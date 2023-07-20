import time
from concurrent.futures import ThreadPoolExecutor


def task_for_thread_pool(name, age, n):
    time.sleep(n)
    return f"name is {name}, age is {age}, sleep {n}s"


def callback(future):
    print(future.result())


executor = ThreadPoolExecutor()
future_task = executor.submit(task_for_thread_pool, "test_name", 16, 1)
future_task.add_done_callback(callback)
