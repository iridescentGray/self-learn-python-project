import asyncio
import functools
import time
from typing import Any, Callable

import aiohttp
from aiohttp import ClientSession

"""
会话级别设置了一个超时，那么它会作用在所有的请求上。
如果在具体发请求又重新设置，以重新设置的为准
"""


def async_timed(func: Callable) -> Callable:
    """
    协程方法执行时间统计

    Returns:
        装饰器本身

    """

    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        print(f"coroutine {func.__name__} 开始执行")
        start = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            total = end - start
            print(f"coroutine {func.__name__} 用 {total} 秒执行完毕")

    return wrapper


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
