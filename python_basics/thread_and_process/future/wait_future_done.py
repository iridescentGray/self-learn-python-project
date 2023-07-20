import time
from concurrent.futures import ThreadPoolExecutor, wait


def task(name, age, n):
    time.sleep(n)
    return f"name is {name}, age is {age}, sleep {n}s"


executor = ThreadPoolExecutor()

future1 = executor.submit(task, "t1", 16, 5)
future2 = executor.submit(task, "t2", 16, 2)
future3 = executor.submit(task, "t3", 15, 4)

# return_when have three options available
# FIRST_COMPLETED
# FIRST_EXCEPTION
# ALL_COMPLETED
fs = wait([future1, future2, future3], return_when="ALL_COMPLETED")
print(f"wait type {type(fs)}")

print(f"fs.done:  {fs.done}")
print(f"fs.not_done:  {fs.not_done}")

for f in fs.done:
    print(f.result())
