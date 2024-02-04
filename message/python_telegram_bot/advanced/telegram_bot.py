import asyncio
import logging
import copy
import threading
from typing import Any, Dict, List, Optional, Union

from telegram import (
    KeyboardButton,
    PhotoSize,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.constants import ParseMode
from telegram.error import BadRequest, NetworkError, TelegramError
from telegram.ext import (
    Application,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    AIORateLimiter,
)
from telegram.error import (
    BadRequest,
    ChatMigrated,
    Conflict,
    Forbidden,
    InvalidToken,
    NetworkError,
    PassportDecryptionError,
    RetryAfter,
    TelegramError,
    TimedOut,
)
from telegram._utils.types import DVInput, FileInput, ODVInput, ReplyMarkup
from telegram._utils.defaultvalue import DEFAULT_NONE

from message_types import RPCMessageType
from rpc_types import RPCSendMsg

logger = logging.getLogger(__name__)


async def tlg_error_callback(update, context: ContextTypes.DEFAULT_TYPE):
    del update
    # Handle error
    try:
        raise context.error  # type: ignore
    except BadRequest:
        logger.error("TLG Error: Bad Request")
    except ChatMigrated:
        logger.error("TLG Error: Chat Migrated")
    except Conflict:
        logger.error("TLG Error: Conflict")
    except Forbidden:
        logger.error("TLG Error: Forbidden/Unauthorized")
    except InvalidToken:
        logger.error("TLG Error: Invalid Token")
    except TimedOut:
        logger.error("TLG Error: Timeout (slow connection issue)")
    except NetworkError:
        logger.error("TLG Error: Network Problem")
    except PassportDecryptionError:
        logger.error("TLG Error: Passport Decryption Error")
    except RetryAfter:
        logger.error("TLG Error: Retry After")
    except TelegramError as error:
        logger.error("TLG Error: %s", str(error))


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
        self._thread = threading.Thread(target=self._init, name="MyTelegram")
        self._thread.start()

    def _init_keyboard(self) -> None:
        """
        Validates the keyboard configuration from telegram config
        section.
        """
        self._keyboard: List[List[Union[str, KeyboardButton]]] = [
            ["/status", "/start", "/stop", "/help"],
        ]

    async def post_init(self, application: Application):
        ...

    async def post_stop(self, application: Application):
        ...

    async def post_shutdown(self, application: Application):
        ...

    def _init_telegram_app(self):
        return (
            Application.builder()
            .token(self._config["telegram"]["token"])
            .rate_limiter(AIORateLimiter(max_retries=3))
            .http_version("1.1")
            .get_updates_http_version("1.1")
            .post_init(self.post_init)
            .post_stop(self.post_stop)
            .post_shutdown(self.post_shutdown)
            .build()
        )

    def _init(self) -> None:
        try:
            self._loop = asyncio.get_running_loop()
        except RuntimeError:
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)

        self._app = self._init_telegram_app()
        self._app.add_error_handler(tlg_error_callback)

        types_handles = []
        command_handles = [
            CommandHandler("start", self._start),
            CommandHandler("stop", self._stop),
            CommandHandler("status", self._status),
            CommandHandler("help", self._help),
        ]
        message_handles = []
        callbacks = []

        for handle in types_handles:
            self._app.add_handler(handle)
        for handle in command_handles:
            self._app.add_handler(handle)
        for handle in message_handles:
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
                allowed_updates=Update.ALL_TYPES,
                # stop_signals=[],  # Necessary as we don't run on the main thread
            )
            self.__is_running = True
            while True:
                await asyncio.sleep(3)
                if not self._app.updater.running:
                    break

    async def user_is_admin(
        self, chat_id: Union[str, int], user_id: Union[str, int]
    ) -> bool:
        """
        Check if the specified user is an Administrator of a group given by IDs
        """
        try:
            group_admins = await self._app.bot.get_chat_administrators(chat_id=chat_id)
        except Exception as error:
            logger.error("[%s] %s", str(chat_id), str(error))
            return False
        for admin in group_admins:
            if user_id == admin.user.id:
                return True
        return False

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
        message, parse_mode = self.compose_message(copy.deepcopy(msg), msg_type)  # type: ignore
        if message:
            asyncio.run_coroutine_threadsafe(
                self._send_msg(
                    self._config["telegram"]["chat_id"],
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
        await self._send_msg(self._config["telegram"]["chat_id"], f"bot {status}")

    async def _start(self, update: Update, context: CallbackContext) -> None:
        """
        Handler for /start.
        :param bot: telegram bot
        :param update: message update
        :return: None
        """
        self.__is_running = True
        keyboard = ReplyKeyboardMarkup(keyboard=self._keyboard, resize_keyboard=True)
        await self._send_msg(
            self._config["telegram"]["chat_id"], f"bot run", reply_markup=keyboard
        )

    async def _stop(self, update: Update, context: CallbackContext) -> None:
        """
        Handler for /stop.
        :param bot: telegram bot
        :param update: message update
        :return: None
        """
        self.__is_running = False
        await self._send_msg(self._config["telegram"]["chat_id"], f"bot stop")

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
        update.edited_message
        await self._send_msg(
            self._config["telegram"]["chat_id"], message, parse_mode=ParseMode.MARKDOWN
        )

    async def _send_msg(
        self,
        chat_id: Union[str, int],
        msg: str,
        parse_mode: str = ParseMode.MARKDOWN,
        disable_web_page_preview: ODVInput[bool] = DEFAULT_NONE,
        disable_notification: bool = False,
        reply_markup: Optional[ReplyMarkup] = None,
        reply_to_message_id: Optional[int] = None,
        protect_content: bool = True,
    ) -> None:
        """
        Send given markdown message
        :param msg: message
        :param bot: alternative bot
        :param parse_mode: telegram parse mode
        :return: None
        """

        try:
            try:
                await self._app.bot.send_message(
                    chat_id,
                    text=msg,
                    parse_mode=parse_mode,
                    reply_markup=reply_markup,
                    disable_web_page_preview=disable_web_page_preview,
                    disable_notification=disable_notification,
                    reply_to_message_id=reply_to_message_id,
                    protect_content=protect_content,
                )
            except NetworkError as network_err:
                # Sometimes the telegram server resets the current connection,
                # if this is the case we send the message again.
                logger.warning(
                    f"Telegram NetworkError: {network_err.message}! Trying one more time."
                )
                await self._app.bot.send_message(
                    chat_id,
                    text=msg,
                    parse_mode=parse_mode,
                    reply_markup=reply_markup,
                    disable_web_page_preview=disable_web_page_preview,
                    disable_notification=disable_notification,
                    reply_to_message_id=reply_to_message_id,
                    protect_content=protect_content,
                )
        except TelegramError as telegram_err:
            logger.warning(
                "TelegramError: %s! Giving up on that message.", telegram_err.message
            )

    async def _delete_msg(self, chat_id: Union[int, str], msg_id: int):
        """Try to remove a telegram message"""
        delete_result: dict = {}
        if msg_id is not None:
            try:
                await self._app.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as error:
                delete_result.update(error=str(error))
                logger.error(f"[%s] %s", str(chat_id), error)
        return delete_result

    async def _send_image(
        self,
        chat_id: Union[int, str],
        photo: Union[FileInput, PhotoSize],
        caption: Optional[str] = None,
        disable_notification: DVInput[bool] = DEFAULT_NONE,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        topic_id: Optional[int] = None,
        **kwargs,
    ):
        """Bot try to send an image message."""
        sent_result: dict = {}
        try:
            msg = await self._app.bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=caption,
                disable_notification=disable_notification,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                parse_mode=parse_mode,
                message_thread_id=topic_id,
                **kwargs,
            )
            sent_result.update(msg=msg)
        except TelegramError as error:
            sent_result.update(error=str(error))
            logger.error("[%s] %s", str(chat_id), str(error))
        return sent_result

    async def _is_message_from_owner(self, update: Update) -> bool:
        """
        is message send from owner
        """
        owner_id = self._config.get("telegram", {}).get("owner_id", None)
        if not owner_id:
            return False
        message = update.message
        if message is None:
            return False
        user = message.from_user
        if user is None:
            return False
        return user.id == owner_id

    @classmethod
    def get_any_msg(cls, update: Update):
        """
        Get Telegram message data from Update.
        there are three type of message inupdate
        """
        msg = getattr(update, "message", None)
        if msg is None:
            msg = getattr(update, "edited_message", None)
        if msg is None:
            msg = getattr(update, "channel_post", None)
        return msg

    @classmethod
    async def is_bot_mentioned(cls, update: Update, context: CallbackContext):
        try:
            message = update.message
            if message == None:
                return False
            if message.chat.type == "private":
                return True

            if (
                message.text is not None
                and ("@" + context.bot.username) in message.text
            ):
                return True

            if message.reply_to_message is not None:
                if message.reply_to_message.from_user.id == context.bot.id:
                    return True
        except:
            return True
        else:
            return False
