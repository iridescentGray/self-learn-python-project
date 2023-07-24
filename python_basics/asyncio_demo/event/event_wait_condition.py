import asyncio
from asyncio import Condition


async def do_work(cond: Condition):
    async with cond:
        print("do_work,get condition lock,then wait notify")
        await cond.wait()
        print("do_work receive notify，get condition lock again")
        await asyncio.sleep(2)
    print("End of work, release lock---------------")


async def fire_event(cond: Condition):
    await asyncio.sleep(3)
    print("fire_event get condition lock,then notify_all")
    async with cond:
        cond.notify_all()


async def main():
    cond = Condition()
    asyncio.create_task(fire_event(cond))
    await asyncio.gather(do_work(cond), do_work(cond))


asyncio.run(main())
