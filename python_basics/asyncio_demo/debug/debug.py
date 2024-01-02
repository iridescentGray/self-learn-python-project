import asyncio
import time


async def sub_task1() -> None:
    time.sleep(1)  # 同步部分,会导致defined
    print("--------------------sub_task1!")


async def sub_task2() -> None:
    print("--------------------Hello!")
    await asyncio.sleep(1)  # 不会导致defined
    print("---------------------Hi")
    await asyncio.sleep(1)


async def sub_task3() -> None:
    await sub_task1()


async def main() -> None:
    t1 = asyncio.create_task(sub_task1())
    t2 = asyncio.create_task(
        sub_task2()
    )  # sub_task2会分别被sub_task1 和 sub_task3中的time.sleep(1)  阻塞两次
    t3 = asyncio.create_task(sub_task3())
    await asyncio.gather(t1, t2, t3)


asyncio.run(main(), debug=True)
