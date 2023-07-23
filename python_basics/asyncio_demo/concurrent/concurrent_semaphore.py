import asyncio
from asyncio import Semaphore


async def operation(sem: Semaphore):
    print("wait Semaphore")
    async with sem:
        print("get Semaphore")
        await asyncio.sleep(3)
    print("release Semaphore ")


async def semaphore_test():
    sem = Semaphore(2)
    await asyncio.gather(*[operation(sem) for _ in range(4)])


asyncio.run(semaphore_test())
