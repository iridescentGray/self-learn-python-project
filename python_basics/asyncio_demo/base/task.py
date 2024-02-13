import asyncio

print(
    f"-----------------------------------------create task ------------------------------------------"
)


async def delay(seconds):
    print(f"Start Sleep {seconds} 秒")
    await asyncio.sleep(seconds)
    print(f"Sleep {seconds} completed")
    return seconds


async def create_task():
    sleep_for_three = asyncio.create_task(delay(2))
    print("sleep_for_three:", sleep_for_three.__class__)
    print("done", sleep_for_three.done())
    # 等到 Task 对象里面的协程运行完毕后，才能往下执行
    result = await sleep_for_three
    print("done", sleep_for_three.done())
    print("Return value:", result)


asyncio.run(create_task())

print(
    f"-----------------------------------------task Simultaneous execution------------------------------------------"
)


async def simultaneous_execution():
    sleep_for_three = asyncio.create_task(delay(2))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(1))

    await sleep_for_three
    await sleep_again
    await sleep_once_more


asyncio.run(simultaneous_execution())
