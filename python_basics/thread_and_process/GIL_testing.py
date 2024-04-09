import time
from multiprocessing import Process
from threading import Thread


def count(to: int):
    start = time.perf_counter()
    counter = 0
    while counter < to:
        counter += 1
    end = time.perf_counter()

    print(f"在 {end - start} 秒内将 counter 增加到 {to}")


def process_test():
    start = time.perf_counter()
    task1 = Process(target=count, args=(100000000,))
    task2 = Process(target=count, args=(100000000,))
    # 启动进程
    task1.start()
    task2.start()

    task1.join()
    task2.join()
    end = time.perf_counter()
    print(f"process_test在 {end - start} 秒内完成")


def thread_test():
    start = time.perf_counter()
    task1 = Thread(target=count, args=(100000000,))
    task2 = Thread(target=count, args=(100000000,))
    task1.start()
    task2.start()
    task1.join()
    task2.join()
    end = time.perf_counter()
    print(f"thread_test在 {end - start} 秒内完成")


if __name__ == "__main__":
    process_test()
    # because of GIL lock,thread_test() performance is Far behind than process_test()
    thread_test()
