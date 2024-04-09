import asyncio
from asyncio import LifoQueue, Queue
from dataclasses import dataclass, field

print(
    "-----------------------------------naive_data_type_in_priority_queue-----------------------------------"
)


@dataclass(order=True)
class WorkItem:
    priority: int
    index: int
    data: str = field(compare=False)


async def worker(queue: Queue):
    while not queue.empty():
        worker_item: WorkItem = await queue.get()
        print(f"处理数据项: {worker_item}")
        queue.task_done()


async def main():
    lifo_queue = LifoQueue()
    work_items = [
        WorkItem(3, 0, "低优先级(1)"),
        WorkItem(3, 1, "低优先级(2)"),
        WorkItem(3, 2, "低优先级(3)"),
        WorkItem(1, 0, "高优先级"),
        WorkItem(2, 0, "中优先级"),
    ]
    worker_task = asyncio.create_task(worker(lifo_queue))
    for work_item in work_items:
        lifo_queue.put_nowait(work_item)

    await asyncio.gather(lifo_queue.join(), worker_task)


asyncio.run(main())
