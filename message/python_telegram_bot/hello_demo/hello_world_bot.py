from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = ""


# 响应/hello消息
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
