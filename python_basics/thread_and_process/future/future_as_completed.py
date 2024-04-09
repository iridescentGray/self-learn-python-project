import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def task(name, age, n):
    time.sleep(n)
    return f"name is {name}, age is {age}, sleep {n}s"


executor = ThreadPoolExecutor()

futures = [
    executor.submit(task, "t1", 16, 5),
    executor.submit(task, "t2", 16, 2),
    executor.submit(task, "t3", 15, 4),
    executor.submit(task, "t4", 19, 3),
    executor.submit(task, "t5", 16, 6),
]

"""
run like asyncio,as_completed()
Whichever task is completed first, return first
"""
for future in as_completed(futures):
    print(future.result())
