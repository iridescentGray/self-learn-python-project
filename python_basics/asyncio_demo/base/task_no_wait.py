import asyncio


async def delay(seconds):
    print(f"Start Sleep {seconds} 秒")
    await asyncio.sleep(seconds)
    print(f"Sleep {seconds} completed")
    return seconds


background_tasks = set()


async def main():
    for i in range(3):
        task = asyncio.create_task(delay(i))
        background_tasks.add(task)
        task.add_done_callback(background_tasks.discard)

    print(background_tasks)
    await asyncio.sleep(3)
    print(background_tasks)


asyncio.run(main())
