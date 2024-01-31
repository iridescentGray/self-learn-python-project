import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor

from python_basics.decorator_demo import async_timed


def do_count_number(to: int) -> int:
    counter = 0
    while counter < to:
        counter += 1
    return counter


@async_timed
async def integration_process_and_gather():
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        numbers = [100000000, 1, 100, 10000, 1000000, 1000, 100000]
        tasks = [
            loop.run_in_executor(process_pool, do_count_number, n) for n in numbers
        ]
        [print(type(task)) for task in tasks]  # _asyncio.Future
        # we can use gather to wait '_asyncio.Future' done
        results = await asyncio.gather(*tasks)
        print(f"integration_hello_world {results}")


@async_timed
async def integration_process_and_as_completed():
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        numbers = [100000000, 1, 100, 10000, 1000000, 1000, 100000]
        tasks = [
            loop.run_in_executor(process_pool, do_count_number, n) for n in numbers
        ]
        for result in asyncio.as_completed(tasks):
            print(await result)


if __name__ == "__main__":
    asyncio.run(integration_process_and_gather())
    asyncio.run(integration_process_and_as_completed())
