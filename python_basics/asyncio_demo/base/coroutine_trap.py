import asyncio


from python_basics.decorator_demo import async_timed

"""
以下场景使用协程却得不到提升:
	第一: 代码是 CPU 密集
    第二：代码虽然是 IO 密集，但 IO 是阻塞 IO，而不是非阻塞 IO
"""


@async_timed
async def cpu_bound_work():
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter


@async_timed
async def cpu_dense():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    # 即便创建任务，也不会提升效率
    task_three = asyncio.create_task(asyncio.sleep(4))
    await task_one
    await task_two
    await task_three


asyncio.run(cpu_dense())
