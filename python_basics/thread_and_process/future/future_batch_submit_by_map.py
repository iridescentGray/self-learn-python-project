import time
from concurrent.futures import ThreadPoolExecutor


def task(name, age, n):
    time.sleep(n)
    return f"name is {name}, age is {age}, sleep {n}s"


executor = ThreadPoolExecutor()

results = executor.map(
    task, ["t1", "t2", "t3", "t4", "t5"], [16, 16, 15, 19, 16], [5, 2, 4, 3, 1]
)

print(results)

for result in results:
    print(result)
