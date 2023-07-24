import asyncio
from asyncio import Condition

initialized = False


async def change_initial(cond: Condition):
    async with cond:
        global initialized
        await asyncio.sleep(3)
        initialized = True
        cond.notify_all()


def is_initialized():
    print(f"initialized is {initialized}")
    return initialized


async def main():
    cond = Condition()
    print("start to wait for")
    async with cond:
        asyncio.create_task(change_initial(cond))
        await cond.wait_for(is_initialized)
    print("end to wait for")


asyncio.run(main())
