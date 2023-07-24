import asyncio
from asyncio import Queue, PriorityQueue
from dataclasses import dataclass, field
from typing import Tuple

print("-----------------------------------naive_data_type_in_priority_queue-----------------------------------")


async def worker(queue: Queue):
    while not queue.empty():
        worker_item: Tuple[int, str] = await queue.get()
        print(f"处理数据项: {worker_item}")
        queue.task_done()


async def naive_data_type_in_queue():
    priority_queue = PriorityQueue()
    work_items = [(3, "低优先级"), (1, "高优先级"), (2, "中优先级")]
    worker_task = asyncio.create_task(worker(priority_queue))
    for work_item in work_items:
        priority_queue.put_nowait(work_item)
    await asyncio.gather(priority_queue.join(), worker_task)


asyncio.run(naive_data_type_in_queue())

print("-----------------------------------dataclass_in_priority_queue-----------------------------------")


@dataclass(order=True)
class WorkItem:
    priority: int
    data: str = field(compare=False)


async def dataclass_in_priority_queue():
    priority_queue = PriorityQueue()
    work_items = [WorkItem(3, "低优先级"), WorkItem(1, "高优先级"), WorkItem(2, "中优先级")]
    worker_task = asyncio.create_task(worker(priority_queue))
    for work_item in work_items:
        priority_queue.put_nowait(work_item)

    await asyncio.gather(priority_queue.join(), worker_task)


asyncio.run(dataclass_in_priority_queue())
