import asyncio

counter: int = 0


async def increment():
    global counter
    temp_counter = counter
    temp_counter += 1
    await asyncio.sleep(0.01)
    counter = temp_counter


async def main():
    global counter
    for _ in range(100):
        tasks = [asyncio.create_task(increment()) for _ in range(100)]
        await asyncio.gather(*tasks)
        print(counter)
        assert counter == 100
        # 将 counter 重置为 0，重新开始循环
        counter = 0


asyncio.run(main())
