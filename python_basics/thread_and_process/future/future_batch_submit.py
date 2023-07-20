import time
from concurrent.futures import ThreadPoolExecutor


def task_for_thread_pool(name, age, n):
    time.sleep(n)
    return f"name is {name}, age is {age}, sleep {n}s"


executor = ThreadPoolExecutor()

futures = [
    # this long time future will block behind short time future
    executor.submit(task_for_thread_pool, "batch_submit_test_name4", 16, 4),
    executor.submit(task_for_thread_pool, "batch_submit_test_name2", 16, 2),
    executor.submit(task_for_thread_pool, "batch_submit_test_name3", 16, 3),
    executor.submit(task_for_thread_pool, "batch_submit_test_name1", 16, 1),
]
for future in futures:
    print(f"future.done() {future.done()}")
    print(f"future.running() {future.running()}")
    print(future.result())
    print("*" * 100)
