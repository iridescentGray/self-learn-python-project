import asyncio


async def error_delay(seconds):
    await asyncio.sleep(seconds)
    if seconds >= 2:
        raise ValueError(f"我出错了 seconds = {seconds}")
    return f"我睡了 {seconds} 秒"


print(
    "------------------------------------cancel_if_first_exception_appear----------------------------------------"
)


async def cancel_if_first_exception_appear():
    tasks = [
        asyncio.create_task(error_delay(seconds), name=f"睡了 {seconds} 秒的任务")
        for seconds in range(1, 5)
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    print(f"已完成的任务数: {len(done)}")
    print(f"未完成的任务数: {len(pending)}")

    for done_task in done:
        exc = done_task.exception()
        if exc:
            print(f"error is {exc}")
        else:
            print(done_task.result())

    for t in pending:
        t.cancel()
    # 阻塞 3 秒
    await asyncio.sleep(3)


asyncio.run(cancel_if_first_exception_appear())
