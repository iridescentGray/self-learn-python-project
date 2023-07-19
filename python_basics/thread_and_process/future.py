import time
from concurrent.futures import ThreadPoolExecutor


def task_for_thread_pool(name, age, n):
    time.sleep(n)
    return f"name is {name}, age is {age}, sleep {n}s"


def callback(future):
    print(future.result())


def get_future_and_add_callback():
    executor = ThreadPoolExecutor()
    future = executor.submit(task_for_thread_pool, "test_name", 16, 1)
    future.add_done_callback(callback)


def batch_submit():
    executor = ThreadPoolExecutor()

    futures = [executor.submit(task_for_thread_pool, "batch_submit_test_name4", 16, 4),
               executor.submit(task_for_thread_pool, "batch_submit_test_name2", 16, 2),
               executor.submit(task_for_thread_pool, "batch_submit_test_name3", 16, 3),
               executor.submit(task_for_thread_pool, "batch_submit_test_name1", 16, 1),
               ]
    for future in futures:
        print(future.result())


if __name__ == '__main__':
    get_future_and_add_callback()
    batch_submit()
