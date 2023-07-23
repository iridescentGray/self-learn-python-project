import asyncio
from asyncio import Condition


async def do_work(cond: Condition):
    print("wait lock for work")
    async with cond:
        print("已获得锁，然后立即释放")
        # 等待事件触发，一旦成功，重新获取条件锁
        await cond.wait()
        print("再次获得条件锁，继续执行逻辑")
        await asyncio.sleep(1)
    # 退出 async with 语句块后，释放条件锁。
    print("End of work, release lock")


async def fire_event(cond: Condition):
    await asyncio.sleep(5)
    print("get condition lock")
    async with cond:
        # 通知所有任务：事件已经发生
        cond.notify_all()
    print("release condition lock")


async def main():
    cond = Condition()
    asyncio.create_task(fire_event(cond))
    await asyncio.gather(do_work(cond))


asyncio.run(main())
