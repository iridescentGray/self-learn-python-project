import asyncio


async def delay(seconds):
    print(f"Start Sleep {seconds} 秒")
    await asyncio.sleep(seconds)
    print("Sleep completed")
    return seconds


print(
    "-----------------------------------------create event loop------------------------------------------"
)

new_loop = asyncio.new_event_loop()
try:
    new_loop.run_until_complete(delay(2))
finally:
    new_loop.close()

print(
    "----------------------------------get running loop mode 1：get_running_loop------------------------------"
)


def some_func():
    print("我将稍后被调用")


async def get_running_loop_case():
    # 协程需要扔到事件循环里面运行，而当协程运行的时候，也可以获取所在的事件循环
    loop = asyncio.get_running_loop()
    loop.call_soon(some_func)
    await asyncio.sleep(1)


running_loop_case_loop = asyncio.new_event_loop()
try:
    running_loop_case_loop.run_until_complete(get_running_loop_case())
finally:
    running_loop_case_loop.close()


print(
    "----------------------------------get running loop mode2：get_event_loop------------------------------"
)
get_event_loop_method_loop = asyncio.get_event_loop()
get_event_loop_method_loop.close()
print(
    "----------------------------------View unfinished tasks in event loop------------------------------"
)


async def main1():
    await asyncio.sleep(1)
    print("我是 main1")


async def main2():
    await asyncio.sleep(2)
    print("我是 main2")


async def main3():
    await asyncio.sleep(3)
    print("我是 main3")


view_unfinished_tasks_in_event_loop = asyncio.new_event_loop()
try:
    view_unfinished_tasks_in_event_loop.create_task(
        main1(), name="main1"
    )  # 创建任务时可以给任务起个名字
    view_unfinished_tasks_in_event_loop.create_task(main2(), name="main2")
    view_unfinished_tasks_in_event_loop.create_task(main3(), name="main3")

    view_unfinished_tasks_in_event_loop.run_until_complete(asyncio.sleep(1.5))

    # 所以此时 main1() 一定运行完了，但 main2() 和 main3() 没有
    # 通过 asyncio.all_tasks(loop) 可以查看当前尚未运行完毕的所有任务
    unfinished_tasks = asyncio.all_tasks(view_unfinished_tasks_in_event_loop)
    # 返回一个集合，显然里面就是 main2 和 main3 两个没有完成的任务
    print(unfinished_tasks)

    t1 = unfinished_tasks.pop()
    t2 = unfinished_tasks.pop()
    #  main2 main3
    print(t1.get_name(), t2.get_name())

    # 继续让它完成
    view_unfinished_tasks_in_event_loop.run_until_complete(t1)
    view_unfinished_tasks_in_event_loop.run_until_complete(t2)

finally:
    view_unfinished_tasks_in_event_loop.close()
