import asyncio
from pprint import pprint

"""
对于asyncio.gather、wait，如果某个任务出现异常，那么异常会向上抛给 await 所在的位置
  如果不希望异常抛出，可以指定return_exceptions的参数为 True，出现异常的任务会直接视为已完成
  如果将抛出的异常捕获，其它任务不会受到影响
"""

print(f"------------------------catch_error_will_not_affect_other_task-------------------------------------------")


async def normal_running():
    await asyncio.sleep(3)
    return "normal_running() completed, not affected by raise_error() Error"


async def raise_error():
    raise ValueError("出错啦")


async def catch_error_will_not_affect_other_task():
    try:
        await asyncio.gather(normal_running(), raise_error())
    except Exception as e:
        pprint(f"run error is {e}")

    results = await asyncio.gather(*[task for task in asyncio.all_tasks()
                                     if task.get_coro().__name__ != "catch_error_will_not_affect_other_task"])
    print(results)


asyncio.run(catch_error_will_not_affect_other_task())

print(f"----------------------------------handle_gather_error-------------------------------------------")


async def handle_gather_error():
    results = await asyncio.gather(normal_running(), raise_error(),
                                   return_exceptions=True)
    # Collect both results and exception
    for result in results:
        print(result)
        print(type(result))


asyncio.run(handle_gather_error())

print(f"----------------------------------handle_wait_error-------------------------------------------")


async def error_delay(seconds):
    await asyncio.sleep(seconds)
    if seconds >= 2:
        raise ValueError(f"我出错了 seconds = {seconds}")
    return f"我睡了 {seconds} 秒"


async def handle_wait_error():
    tasks = [asyncio.create_task(error_delay(seconds)) for seconds in [1, 3, 2]]
    done, pending = await asyncio.wait(tasks)
    print(f"已完成的任务数: {len(done)}")
    print(f"未完成的任务数: {len(pending)}")

    for done_task in done:
        exc = done_task.exception()
        # 需要先检测异常是否为空,在用result()获取运行结果
        if exc:
            print(f"error is {exc}")
        else:
            print(done_task.result())


asyncio.run(handle_wait_error())
