import asyncio
import functools
import time
from typing import Any, Callable

import aiohttp
from aiohttp import ClientSession


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


"""
大多数基于 aiohttp 的应用程序在整个应用程序内都只使用一个会话，然后将此会话对象传递给需要的函数。
而会话对象有很多方法，用于发出任意数量的 Web 请求，比如 GET、PUT 和 POST 等等，
我们可使用 async with 语法和 aiohttp.ClientSession 以异步上下文管理器的方式来创建会话
"""


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
