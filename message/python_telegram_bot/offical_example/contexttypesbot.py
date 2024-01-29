import logging
from collections import defaultdict
from typing import DefaultDict, Optional, Set

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ExtBot,
    TypeHandler,
)
from tg_config import token

"""
This example showcases how telegram.ext.ContextTypes can be used to customize the context argument of handler and job callbacks.


doc:
https://docs.python-telegram-bot.org/en/v20.7/examples.contexttypesbot.html


feature:
1.self definition ChatData
1.self definition CallbackContext
3.use update.effective_message.edit_text to change old message
4.track all bot users
"""

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


class ChatData:
    """Custom class for chat_data. Here we store data per message."""

    def __init__(self) -> None:
        self.clicks_per_message: DefaultDict[int, int] = defaultdict(int)


class CustomContext(CallbackContext[ExtBot, dict, ChatData, dict]):
    def __init__(
        self,
        application: Application,
        chat_id: Optional[int] = None,
        user_id: Optional[int] = None,
    ):
        super().__init__(application=application, chat_id=chat_id, user_id=user_id)
        self._message_id: Optional[int] = None

    @property
    def bot_user_ids(self) -> Set[int]:
        return self.bot_data.setdefault("user_ids", set())

    @property
    def message_clicks(self) -> Optional[int]:
        if self._message_id:
            return self.chat_data.clicks_per_message[self._message_id]
        return None

    @message_clicks.setter
    def message_clicks(self, value: int) -> None:
        """Allow to change the count"""
        if not self._message_id:
            raise RuntimeError(
                "There is no message associated with this context object."
            )
        self.chat_data.clicks_per_message[self._message_id] = value

    @classmethod
    def from_update(cls, update: object, application: "Application") -> "CustomContext":
        """Override from_update to set _message_id."""
        context = super().from_update(update, application)

        if (
            context.chat_data
            and isinstance(update, Update)
            and update.effective_message
        ):
            # pylint: disable=protected-access
            context._message_id = update.effective_message.message_id

        # Remember to return the object
        return context


async def start(update: Update, context: CustomContext) -> None:
    """Display a message with a button."""
    await update.message.reply_html(
        "This button was clicked <i>0</i> times.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Click me!", callback_data="button")
        ),
    )


async def count_click(update: Update, context: CustomContext) -> None:
    """Update the click count for the message."""
    context.message_clicks += 1
    await update.callback_query.answer()
    await update.effective_message.edit_text(
        f"This button was clicked <i>{context.message_clicks}</i> times.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Click me!", callback_data="button")
        ),
        parse_mode=ParseMode.HTML,
    )


async def print_users(update: Update, context: CustomContext) -> None:
    """Show which users have been using this bot."""
    await update.message.reply_text(
        f"The following user IDs have used this bot: {', '.join(map(str, context.bot_user_ids))}"
    )


async def track_users(update: Update, context: CustomContext) -> None:
    """Store the user id of the incoming update, if any."""
    if update.effective_user:
        context.bot_user_ids.add(update.effective_user.id)


def main() -> None:
    context_types = ContextTypes(context=CustomContext, chat_data=ChatData)
    application = (
        Application.builder().token(token).context_types(context_types).build()
    )
    application.add_handler(TypeHandler(Update, track_users), group=-1)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(count_click))
    application.add_handler(CommandHandler("print_users", print_users))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
