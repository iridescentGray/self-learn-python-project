import asyncio


async def delay(seconds):
    print(f"Start Sleep {seconds} 秒")
    await asyncio.sleep(seconds)
    print(f"Sleep completed")
    return seconds


print(f"-----------------------------------------create event loop------------------------------------------")

new_loop = asyncio.new_event_loop()
try:
    new_loop.run_until_complete(delay(2))
finally:
    new_loop.close()

print(f"----------------------------------get running loop mode 1：get_running_loop------------------------------")


async def some_func():
    print("我将稍后被调用")


async def get_running_loop_case():
    # 协程需要扔到事件循环里面运行，而当协程运行的时候，也可以获取所在的事件循环
    loop = asyncio.get_running_loop()
    loop.call_soon(some_func)
    await asyncio.sleep(2)


running_loop_case_loop = asyncio.new_event_loop()
try:
    running_loop_case_loop.run_until_complete(get_running_loop_case())
finally:
    running_loop_case_loop.close()


print(f"----------------------------------get running loop mode2：get_event_loop------------------------------")

