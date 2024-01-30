"""
This module manage Telegram communication
"""
import asyncio
import json
import logging
import datetime
from copy import deepcopy
from threading import Thread
from typing import Any, Callable, Coroutine, Dict, List, Optional, Union

from telegram import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.constants import MessageLimit, ParseMode
from telegram.error import BadRequest, NetworkError, TelegramError
from telegram.ext import (
    Application,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    TypeHandler,
)
from rpc_types import RPCSendMsg

from message_types import RPCMessageType

MAX_MESSAGE_LENGTH = MessageLimit.MAX_TEXT_LENGTH


logger = logging.getLogger(__name__)


class Telegram:
    def __init__(self, config: dict) -> None:
        self._config: dict = config
        self._app: Application
        self.__is_running: bool
        self._loop: asyncio.AbstractEventLoop
        self._init_keyboard()
        self._start_thread()

    def _start_thread(self):
        """
        Creates and starts the polling thread
        """
        self._thread = Thread(target=self._init, name="MyTelegram")
        self._thread.start()

    def _init_keyboard(self) -> None:
        """
        Validates the keyboard configuration from telegram config
        section.
        """
        self._keyboard: List[List[Union[str, KeyboardButton]]] = [
            ["/status", "/start", "/stop", "/help"],
        ]

    def _init_telegram_app(self):
        return Application.builder().token(self._config["telegram"]["token"]).build()

    def _init(self) -> None:
        try:
            self._loop = asyncio.get_running_loop()
        except RuntimeError:
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)

        self._app = self._init_telegram_app()

        types_handles = []
        command_handles = [
            CommandHandler("status", self._status),
            CommandHandler("start", self._start),
            CommandHandler("stop", self._stop),
            CommandHandler("help", self._help),
        ]
        callbacks = []
        for handle in types_handles:
            self._app.add_handler(handle)

        for handle in command_handles:
            self._app.add_handler(handle)

        for callback in callbacks:
            self._app.add_handler(callback)

        logger.info(
            "telegram is listening for following commands: %s",
            [[x for x in sorted(h.commands)] for h in command_handles],
        )
        self._loop.run_until_complete(self._startup_telegram())

    async def _startup_telegram(self) -> None:
        await self._app.initialize()
        await self._app.start()
        if self._app.updater:
            await self._app.updater.start_polling(
                bootstrap_retries=-1,
                timeout=20,
                # read_latency=60,  # Assumed transmission latency
                drop_pending_updates=True,
                # stop_signals=[],  # Necessary as we don't run on the main thread
            )
            self.__is_running = True
            while True:
                await asyncio.sleep(3)
                if not self._app.updater.running:
                    break

    async def _cleanup_telegram(self) -> None:
        if self._app.updater:
            await self._app.updater.stop()
        await self._app.stop()
        await self._app.shutdown()

    def cleanup(self) -> None:
        """
        Stops all running telegram threads.
        :return: None
        """
        # This can take up to `timeout` from the call to `start_polling`.
        asyncio.run_coroutine_threadsafe(self._cleanup_telegram(), self._loop)
        self._thread.join()

    def compose_message(
        self, msg: Dict[str, Any], msg_type: RPCMessageType
    ) -> Optional[tuple]:
        message = msg
        parse_mode = ParseMode.MARKDOWN
        if msg_type == RPCMessageType.STATUS:
            message = f"*Status:* `{msg['status']}`"
        elif msg_type == RPCMessageType.GETCODE:
            message = "input the code:"
            parse_mode = ParseMode.HTML
        return message, parse_mode

    def send_msg(self, msg: RPCSendMsg) -> None:
        """Send a message to telegram channel"""
        msg_type = msg["type"]
        message, parse_mode = self.compose_message(deepcopy(msg), msg_type)  # type: ignore
        if message:
            asyncio.run_coroutine_threadsafe(
                self._send_msg(
                    message,
                    parse_mode=parse_mode,
                    disable_notification=False,
                ),
                self._loop,
            )

    async def _status(self, update: Update, context: CallbackContext) -> None:
        """
        Handler for /status.
        Returns the current TradeThread status
        :param bot: telegram bot
        :param update: message update
        :return: None
        """
        status = "is running" if self.__is_running else "not run"
        await self._send_msg(f"bot {status}")

    async def _start(self, update: Update, context: CallbackContext) -> None:
        """
        Handler for /start.
        :param bot: telegram bot
        :param update: message update
        :return: None
        """
        self.__is_running = True
        await self._send_msg(f"bot run")

    async def _stop(self, update: Update, context: CallbackContext) -> None:
        """
        Handler for /stop.
        :param bot: telegram bot
        :param update: message update
        :return: None
        """
        self.__is_running = False
        await self._send_msg(f"bot stop")

    async def _help(self, update: Update, context: CallbackContext) -> None:
        """
        Handler for /help.
        Show commands of the bot
        :param bot: telegram bot
        :param update: message update
        :return: None
        """
        message = (
            "_Bot Control_\n"
            "------------\n"
            "*/start:* `Starts the bot`\n"
            "*/stop:* Stops the bot\n"
            "*/status:* `show bot status`\n"
            "*/help:* `This help message`"
        )

        await self._send_msg(message, parse_mode=ParseMode.MARKDOWN)

    async def _update_msg(
        self,
        query: CallbackQuery,
        msg: str,
        callback_path: str = "",
        reload_able: bool = False,
        parse_mode: str = ParseMode.MARKDOWN,
    ) -> None:
        if reload_able:
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Refresh", callback_data=callback_path)],
                ]
            )
        else:
            reply_markup = InlineKeyboardMarkup([[]])
        msg += f"\nUpdated: {datetime.datetime.now().ctime()}"
        if not query.message:
            return
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        try:
            await self._app.bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=msg,
                parse_mode=parse_mode,
                reply_markup=reply_markup,
            )
        except BadRequest as e:
            if "not modified" in e.message.lower():
                pass
            else:
                logger.warning("TelegramError: %s", e.message)
        except TelegramError as telegram_err:
            logger.warning(
                "TelegramError: %s! Giving up on that message.", telegram_err.message
            )

    async def _send_msg(
        self,
        msg: str,
        parse_mode: str = ParseMode.MARKDOWN,
        disable_notification: bool = False,
        keyboard: Optional[List[List[InlineKeyboardButton]]] = None,
        callback_path: str = "",
        reload_able: bool = True,
        query: Optional[CallbackQuery] = None,
    ) -> None:
        """
        Send given markdown message
        :param msg: message
        :param bot: alternative bot
        :param parse_mode: telegram parse mode
        :return: None
        """
        # reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]
        # if query:
        #     await self._update_msg(
        #         query=query,
        #         msg=msg,
        #         parse_mode=parse_mode,
        #         callback_path=callback_path,
        #         reload_able=reload_able,
        #     )
        #     return
        reply_markup = ReplyKeyboardMarkup(self._keyboard, resize_keyboard=True)
        try:
            try:
                await self._app.bot.send_message(
                    self._config["telegram"]["chat_id"],
                    text=msg,
                    parse_mode=parse_mode,
                    reply_markup=reply_markup,
                    disable_notification=disable_notification,
                )
            except NetworkError as network_err:
                # Sometimes the telegram server resets the current connection,
                # if this is the case we send the message again.
                logger.warning(
                    f"Telegram NetworkError: {network_err.message}! Trying one more time."
                )
                await self._app.bot.send_message(
                    self._config["telegram"]["chat_id"],
                    text=msg,
                    parse_mode=parse_mode,
                    reply_markup=reply_markup,
                    disable_notification=disable_notification,
                )
        except TelegramError as telegram_err:
            logger.warning(
                "TelegramError: %s! Giving up on that message.", telegram_err.message
            )


if __name__ == "__main__":
    config = {
        "telegram": {
            "chat_id": "",
            "token": "",
        }
    }
    bot = Telegram(config)
