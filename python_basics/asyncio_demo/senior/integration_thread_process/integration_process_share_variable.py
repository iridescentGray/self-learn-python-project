import asyncio
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value

lock_shared_counter: Value
unlock_shared_counter: Value


def init_unlock_shared_counter(counter: Value):
    global unlock_shared_counter
    unlock_shared_counter = counter


def unlock_increment():
    unlock_shared_counter.value += 1


async def process_unlock_share_variable():
    counter = Value("i", 0)
    # 告诉进程池，创建进程的时候使用参数 counter 执行 init_lock_shared_counter 函数
    with ProcessPoolExecutor(initializer=init_unlock_shared_counter, initargs=(counter,)) as pool:
        loop = asyncio.get_running_loop()
        tasks = [loop.run_in_executor(pool, unlock_increment) for n in range(0, 1000)]
        await asyncio.gather(*tasks)
    print(counter.value)


def init_lock_shared_counter(counter: Value):
    global lock_shared_counter
    lock_shared_counter = counter


def lock_increment():
    with lock_shared_counter.get_lock():
        lock_shared_counter.value += 1


async def process_lock_share_variable():
    counter = Value("i", 0)
    # 告诉进程池，创建进程的时候使用参数 counter 执行 init_lock_shared_counter 函数
    with ProcessPoolExecutor(initializer=init_lock_shared_counter, initargs=(counter,)) as pool:
        loop = asyncio.get_running_loop()
        tasks = [loop.run_in_executor(pool, lock_increment) for n in range(0, 1000)]
        await asyncio.gather(*tasks)
        print(counter.value)


if __name__ == '__main__':
    print(f"----------------------------------process_unlock_share_variable------------------------------------")
    asyncio.run(process_unlock_share_variable())
    print(f"----------------------------------process_lock_share_variable------------------------------------")
    asyncio.run(process_lock_share_variable())
