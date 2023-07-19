import asyncio


async def delay(seconds):
    print(f"Start Sleep {seconds} 秒")
    await asyncio.sleep(seconds)
    print(f"Sleep completed")
    return seconds


async def error_delay(seconds):
    await asyncio.sleep(seconds)
    if seconds >= 2:
        raise ValueError(f"我出错了 seconds = {seconds}")
    return f"我睡了 {seconds} 秒"


print(f"-----------------------------------------cancel task-------------------------------------------------")


async def cancel_task():
    long_task = asyncio.create_task(delay(4))
    seconds_elapsed = 0

    while not long_task.done():
        print("任务尚未完成")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        # 时间超过 5 秒，取消任务
        if seconds_elapsed == 2:
            long_task.cancel()
    try:
        # await 一个已经取消的任务或await 的时候任务被取消，会引发 asyncio.CancelledError
        await long_task
    except asyncio.CancelledError:
        print("任务被取消")


asyncio.run(cancel_task())

print(f"---------------------------------wait_task_time_out_the_auto_cancel------------------------------------------")


async def wait_task_time_out_the_auto_cancel():
    delay_task = asyncio.create_task(delay(3))
    try:
        await asyncio.wait_for(delay_task, 2)
    except asyncio.TimeoutError:
        print("超时")
        # 超时后会被自动取消
        print("是否被取消:", delay_task.cancelled())


asyncio.run(wait_task_time_out_the_auto_cancel())

print(f"------------------------------time_out_shield_for_not_auto_cancel----------------------------------------")


async def time_out_shield_for_not_auto_cancel():
    delay_task = asyncio.create_task(delay(2))
    try:
        # 通过 asyncio.shield 将 delay_task 保护起来
        await asyncio.wait_for(asyncio.shield(delay_task), 1)
    except asyncio.TimeoutError:
        print("超时")
        # 超时依旧会引发 TimeoutError，但任务不会被取消了，因为 asyncio.shield 会将取消请求忽略掉
        print("否被取消:", delay_task.cancelled())
        # 从出现超时的地方，还可以继续执行
        result = await delay_task
        print("返回值:", result)


asyncio.run(time_out_shield_for_not_auto_cancel())
