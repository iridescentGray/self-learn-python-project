import asyncio
from asyncio import Lock

lock = Lock()


async def a():
    print("a wait lock")
    async with lock:
        print("a get lock")
        await asyncio.sleep(3)
    print("a release lock")


async def b():
    print("b wait lock")
    async with lock:
        print("b get lock")
        await asyncio.sleep(3)
    print("b release lock")


async def main():
    await asyncio.gather(a(), b())


asyncio.run(main())
