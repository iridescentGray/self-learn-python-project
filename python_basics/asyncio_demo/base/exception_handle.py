import asyncio


async def raise_exc():
    raise ValueError("出错啦")


print(
    "-----------------------------------not_throw_exception_if_only_create_task-----------------------------------"
)


async def not_throw_exception_if_only_create_task():
    # not throw but will print on console
    asyncio.create_task(raise_exc())
    await asyncio.sleep(2)


asyncio.run(not_throw_exception_if_only_create_task())
print("----------print error but not influence execute-----------")
print(
    "-----------------------------------not_throw_exception_if_invoke_exception-----------------------------------"
)


async def not_throw_exception_if_invoke_exception():
    task = asyncio.create_task(raise_exc())
    await asyncio.sleep(1)
    print(task.exception())
    print(task.exception().__class__)


asyncio.run(not_throw_exception_if_invoke_exception())

print(
    "-----------------------------------throw_exception_if_await-----------------------------------"
)


async def throw_exception_if_await():
    task = asyncio.create_task(raise_exc())
    await asyncio.sleep(1)
    try:
        await task
    except Exception as e:
        print("捕获抛出的异常")
        raise e


asyncio.run(throw_exception_if_await())
