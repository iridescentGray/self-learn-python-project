import asyncio

import aiohttp
from aiohttp import ClientSession

from python_basics.decorator_demo import async_timed

"""
会话级别设置了一个超时，那么它会作用在所有的请求上。
如果在具体发请求又重新设置，以重新设置的为准
"""


async def fetch_status(session: ClientSession, url: str):
    timeout = aiohttp.ClientTimeout(1)
    async with session.get(url, timeout=timeout) as response:
        return response.status


@async_timed
async def main():
    timeout = aiohttp.ClientTimeout(3)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        url = "https://hadoop.apache.org"
        status = await fetch_status(session, url)
        print(f"status is {status}")


asyncio.run(main())
