import asyncio
import contextlib
import logging
from typing import NoReturn

from telegram import Bot, Update
from telegram.error import Forbidden, NetworkError
from tg_config import token

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

"""
doc:
https://docs.python-telegram-bot.org/en/v20.7/examples.rawapibot.html

feature:
1.

"""


async def echo(bot: Bot, update_id: int) -> int:
    updates = await bot.get_updates(
        offset=update_id, timeout=10, allowed_updates=Update.ALL_TYPES
    )
    for update in updates:
        next_update_id = update.update_id + 1

        if update.message and update.message.text:
            logger.info("Found message %s!", update.message.text)
            await update.message.reply_text(update.message.text)
        return next_update_id
    return update_id


async def main() -> NoReturn:
    async with Bot(token) as bot:
        try:
            update_id = (await bot.get_updates())[0].update_id
        except IndexError:
            update_id = None

        logger.info("listening for new messages...")
        while True:
            try:
                update_id = await echo(bot, update_id)
            except NetworkError:
                await asyncio.sleep(1)
            except Forbidden:
                update_id += 1


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
