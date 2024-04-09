from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    InlineQueryHandler,
    MessageHandler,
    filters,
)
from tg_config import token


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name} {update.effective_user.last_name}"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Return the way you came.: {update.message.text}",
    )


#  inline bot https://core.telegram.org/bots/inline
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = " ".join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


# 把用户的输入改成大写
async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title="uppercase message",
            input_message_content=InputTextMessageContent(query.upper()),
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )


app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("caps", caps))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(InlineQueryHandler(inline_caps))
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
app.add_handler(MessageHandler(filters.COMMAND, unknown))


app.add_handler(echo_handler)

print("run!")
app.run_polling()
