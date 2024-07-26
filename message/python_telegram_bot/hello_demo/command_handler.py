from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from tg_config import token


async def commond_param(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    print(type(context.args))
    print(context.args)


def main():
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("commond_param", commond_param))
    print("run!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
