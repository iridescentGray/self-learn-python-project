import asyncio
import functools
import time
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


"""
以下场景使用协程却得不到提升:
第二：代码虽然是 IO 密集，但 IO 是阻塞 IO，而不是非阻塞 IO
"""


@async_timed
async def cpu_bound_work():
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter


@async_timed
async def cpu_dense():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    # 即便创建任务，也不会提升效率
    task_three = asyncio.create_task(asyncio.sleep(4))
    await task_one
    await task_two
    await task_three


asyncio.run(cpu_dense())
