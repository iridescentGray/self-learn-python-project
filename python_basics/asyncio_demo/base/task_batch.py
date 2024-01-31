import asyncio
from pprint import pprint

from python_basics.decorator_demo import async_timed


async def delay(seconds):
    await asyncio.sleep(seconds)
    return f"我睡了 {seconds} 秒"


print(
    f"-------------------------------use_create_task_create_batch_await_task------------------------------------"
)


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

print(
    f"----------------------------------use_gather_create_batch_await_task-------------------------------------"
)


@async_timed
async def use_gather_create_batch_await_task():
    tasks = [asyncio.sleep(2) for _ in range(100)]
    status_codes = await asyncio.gather(*tasks)
    print(type(status_codes))
    print(len(status_codes))


asyncio.run(use_gather_create_batch_await_task())

print(
    f"------------------------------------------gather_task_group---------------------------------------------"
)


@async_timed
async def gather_task_group():
    gather1 = asyncio.gather(
        *[asyncio.sleep(second, result=f"我睡了 {second} 秒") for second in (3, 1, 2)]
    )
    gather2 = asyncio.gather(
        *[asyncio.sleep(second, result=f"我睡了 {second} 秒") for second in (1, 1, 1)]
    )
    # 多个gather可以拼接，执行结果也是分组的
    results = await asyncio.gather(gather1, gather2, asyncio.sleep(3, "我睡了 3 秒"))
    pprint(results)


asyncio.run(gather_task_group())

print(
    f"----------------------------------use_as_completed_create_task------------------------------------------"
)


@async_timed
async def use_as_completed_create_task():
    tasks = [asyncio.create_task(delay(seconds)) for seconds in (3, 1, 2, 4)]
    as_completed_result = asyncio.as_completed(tasks)
    print(type(as_completed_result))  # <class 'generator'>
    for finished_task in as_completed_result:
        print(type(finished_task))
        # if you want to handle error,use try except at here
        print(await finished_task)


asyncio.run(use_as_completed_create_task())

print(
    f"-------------------------------timeout_for_as_completed_task-----------------------------------------"
)


@async_timed
async def timeout_for_as_completed_task():
    tasks = [asyncio.create_task(delay(seconds)) for seconds in (1, 3, 4)]
    for finished_task in asyncio.as_completed(tasks, timeout=2):
        try:
            print(await finished_task)
        except asyncio.TimeoutError:
            # 即使抛出TimeoutError，但未完成的任务不会受到影响，它们仍然在后台执行
            print("超时啦")


asyncio.run(timeout_for_as_completed_task())

print(
    f"-------------------------------use_wait_batch_wait_task-----------------------------------------"
)


async def use_wait_batch_wait_task():
    tasks = [asyncio.create_task(delay(seconds)) for seconds in (3, 2, 4)]
    # 和 gather 一样，默认会等待所有任务都完成
    done, pending = await asyncio.wait(tasks, timeout=3)
    print(f"已完成的任务数: {len(done)}")
    print(f"未完成的任务数: {len(pending)}")

    for done_task in done:
        print(await done_task)


asyncio.run(use_wait_batch_wait_task())

print(
    f"-------------------------------wait_first_task_done_then-----------------------------------------"
)


async def wait_first_task_done_then():
    tasks = [asyncio.create_task(delay(seconds)) for seconds in range(1, 4)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"已完成的任务数: {len(done)}")
    print(f"未完成的任务数: {len(pending)}")


asyncio.run(wait_first_task_done_then())
