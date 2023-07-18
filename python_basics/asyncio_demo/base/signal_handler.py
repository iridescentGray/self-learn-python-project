import asyncio
import signal

"""
run this case in terminal,don't in pycharm
"""


def cancel_tasks():
    print("捕获到信号 SIGINT")
    unfinished_tasks = asyncio.all_tasks()
    print(f"要取消 {len(unfinished_tasks)} 个任务")
    for t in unfinished_tasks:
        t.cancel()


async def read_signal():
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)
    loop.add_signal_handler(signal.SIGTERM, cancel_tasks)
    await asyncio.sleep(8)


asyncio.run(read_signal())
