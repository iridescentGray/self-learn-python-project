import asyncio
from pprint import pprint

print(f"------------------------catch_error_will_not_affect_other_task-------------------------------------------")

"""
一个任务出错，那么将异常捕获之后，其它任务不会受到影响
"""


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

print(f"------------------------handle_gather_error-------------------------------------------")


async def handle_gather_error():
    results = await asyncio.gather(normal_running(), raise_error(),
                                   return_exceptions=True)
    for result in results:
        print(result)
        print(type(result))


asyncio.run(handle_gather_error())
