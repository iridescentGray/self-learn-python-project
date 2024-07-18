import asyncio
import functools
import time
from asyncio.events import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable


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


def do_count_number(to: int) -> int:
    counter = 0
    while counter < to:
        counter += 1
    return counter


@async_timed
async def integration_thread_and_gather():
    with ThreadPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        numbers = [100000000, 1, 100, 10000, 1000000, 1000, 100000]
        tasks = [
            loop.run_in_executor(process_pool, do_count_number, n) for n in numbers
        ]
        [print(type(task)) for task in tasks]  # _asyncio.Future
        # we can use gather to wait '_asyncio.Future' done
        results = await asyncio.gather(*tasks)
        print(f"integration_hello_world {results}")


if __name__ == "__main__":
    asyncio.run(integration_thread_and_gather())
