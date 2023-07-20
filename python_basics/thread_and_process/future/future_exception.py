from concurrent.futures import ThreadPoolExecutor


def task1():
    1 / 0


def task2():
    pass


executor = ThreadPoolExecutor(max_workers=2)

future1 = executor.submit(task1)
future2 = executor.submit(task2)
# Exceptions will be saved to future and can be obtained through future.exception()
print(future1.exception())  # division by zero
print(future2.exception())  # None

# 或者
try:
    future1.result()
except Exception as e:
    print(f"except exception {e}")
