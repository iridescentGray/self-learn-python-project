import time
from concurrent.futures import ThreadPoolExecutor


def task(name, age, n):
    time.sleep(n)
    print(f"name is {name}, age is {age}, sleep {n}s")


executor = ThreadPoolExecutor()

future1 = executor.submit(task, "t1", 16, 1)
future2 = executor.submit(task, "t2", 16, 2)
future3 = executor.submit(task, "t3", 15, 4)

# cancel fail,because can't cancel already running task
print(future3.cancel())
