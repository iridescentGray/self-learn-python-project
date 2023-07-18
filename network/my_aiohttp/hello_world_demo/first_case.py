import asyncio

import aiohttp
from aiohttp import ClientSession

from python_basics.decorator import async_timed


async def fetch_status(session: ClientSession, url: str):
    async with session.get(url) as response:
        return response.status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://hadoop.apache.org"
        status = await fetch_status(session, url)
        print(f"status is {status}")


asyncio.run(main())
