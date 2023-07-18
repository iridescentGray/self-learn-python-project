import asyncio
from pprint import pprint

from python_basics.decorator import async_timed

print(f"-------------------------------use_create_task_create_batch_await_task------------------------------------")


@async_timed
async def use_create_task_create_batch_await_task():
    tasks = []
    for second in (2, 2, 2):
        # 丢到事件循环里面即可，不要刚丢进去就 await
        task = asyncio.create_task(asyncio.sleep(second))
        tasks.append(task)
    for task in tasks:
        await task


asyncio.run(use_create_task_create_batch_await_task())

print(f"----------------------------------use_gather_create_batch_await_task-------------------------------------")


@async_timed
async def use_gather_create_batch_await_task():
    tasks = [asyncio.sleep(2) for _ in range(100)]
    status_codes = await asyncio.gather(*tasks)
    print(type(status_codes))
    print(len(status_codes))


asyncio.run(use_gather_create_batch_await_task())

print(f"----------------------------------gather_task_group-------------------------------------")


@async_timed
async def gather_task_group():
    gather1 = asyncio.gather(*[asyncio.sleep(second, result=f"我睡了 {second} 秒")
                               for second in (3, 1, 2)])
    gather2 = asyncio.gather(*[asyncio.sleep(second, result=f"我睡了 {second} 秒")
                               for second in (1, 1, 1)])
    # 多个gather可以拼接，执行结果也是分组的
    results = await asyncio.gather(gather1, gather2, asyncio.sleep(3, "我睡了 3 秒"))
    pprint(results)


asyncio.run(gather_task_group())


