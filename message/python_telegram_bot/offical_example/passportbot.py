import logging
from pathlib import Path

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters
from tg_config import token

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

"""
doc:
https://docs.python-telegram-bot.org/en/v20.7/examples.passportbot.html
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Telegram-Passport

feature:
1.
"""


async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Downloads and prints the received passport data."""
    passport_data = update.message.passport_data
    if passport_data.decrypted_credentials.nonce != "thisisatest":
        return

    for data in passport_data.decrypted_data:  # This is where the data gets decrypted
        if data.type == "phone_number":
            print("Phone: ", data.phone_number)
        elif data.type == "email":
            print("Email: ", data.email)
        if data.type in (
            "personal_details",
            "passport",
            "driver_license",
            "identity_card",
            "internal_passport",
            "address",
        ):
            print(data.type, data.data)
        if data.type in (
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
        ):
            print(data.type, len(data.files), "files")
            for file in data.files:
                actual_file = await file.get_file()
                print(actual_file)
                await actual_file.download_to_drive()
        if (
            data.type
            in ("passport", "driver_license", "identity_card", "internal_passport")
            and data.front_side
        ):
            front_file = await data.front_side.get_file()
            print(data.type, front_file)
            await front_file.download_to_drive()
        if data.type in ("driver_license" and "identity_card") and data.reverse_side:
            reverse_file = await data.reverse_side.get_file()
            print(data.type, reverse_file)
            await reverse_file.download_to_drive()
        if (
            data.type
            in ("passport", "driver_license", "identity_card", "internal_passport")
            and data.selfie
        ):
            selfie_file = await data.selfie.get_file()
            print(data.type, selfie_file)
            await selfie_file.download_to_drive()
        if data.translation and data.type in (
            "passport",
            "driver_license",
            "identity_card",
            "internal_passport",
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
        ):
            print(data.type, len(data.translation), "translation")
            for file in data.translation:
                actual_file = await file.get_file()
                print(actual_file)
                await actual_file.download_to_drive()


def main() -> None:
    private_key = Path("private.key")
    application = (
        Application.builder().token(token).private_key(private_key.read_bytes()).build()
    )
    application.add_handler(MessageHandler(filters.PASSPORT_DATA, msg))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
