import logging
from typing import List, Tuple, cast

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    PicklePersistence,
)

from tg_config import token


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


"""
doc:
https://docs.python-telegram-bot.org/en/v20.7/examples.arbitrarycallbackdatabot.html

feature:
1.

"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number_list: List[int] = []
    await update.message.reply_text(
        "Please choose:", reply_markup=build_keyboard(number_list)
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Use /start to test this bot. Use /clear to clear the stored data so that you can see "
        "what happens, if the button data is not available. "
    )


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Clears the callback data cache"""
    context.bot.callback_data_cache.clear_callback_data()
    context.bot.callback_data_cache.clear_callback_queries()
    await update.effective_message.reply_text("All clear!")


def build_keyboard(current_list: List[int]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup.from_column(
        [
            InlineKeyboardButton(str(i), callback_data=(i, current_list))
            for i in range(1, 6)
        ]
    )


async def list_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    number, number_list = cast(Tuple[int, List[int]], query.data)
    number_list.append(number)

    await query.edit_message_text(
        text=f"So far you've selected {number_list}. Choose the next item:",
        reply_markup=build_keyboard(number_list),
    )
    context.drop_callback_data(query)


async def handle_invalid_button(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Informs the user that the button is no longer available."""
    await update.callback_query.answer()
    await update.effective_message.edit_text(
        "Sorry, I could not process this button click 😕 Please send /start to get a new keyboard."
    )


def main() -> None:
    persistence = PicklePersistence(filepath="arbitrarycallbackdatabot")
    application = (
        Application.builder()
        .token(token)
        .persistence(persistence)
        .arbitrary_callback_data(True)
        .build()
    )
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear))

    application.add_handler(CallbackQueryHandler(list_button))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
