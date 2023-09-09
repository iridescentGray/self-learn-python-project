import asyncio
import functools
import inspect
import logging
import time
from multiprocessing import RLock
from typing import Callable, Any


def count_execute_time():
    """
    方法执行时间统计装饰器
    Args:
        text:  自定义文本

    Returns:
        装饰器本身

    """

    def wrapper_func(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            logging.info(f"methods: {fn.__name__} 开始执行")
            start = time.perf_counter()
            res = fn(*args, **kwargs)
            end = time.perf_counter()
            logging.info(
                f"methods: {fn.__name__} ,运行共计耗时: {end - start} s"
            )
            return res

        return wrapper

    return wrapper_func


def async_timed(func: Callable) -> Callable:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        print(f"coroutine {func.__name__} 开始执行")
        start = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            total = end - start
            print(f"coroutine {func.__name__} 用 {total} 秒执行完毕")

    return wrapper


def singleton(cls):
    """
    线程安全的单例装饰器，用于装饰class
    :param cls: 类
    :return: 单例
    """
    instances = {}
    locker = RLock()

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


def retry(times, exceptions):
    """
    Retry Decorator

    :param times: The number of times to repeat the wrapped function/method
    :type times: Int

    :param exceptions: Lists of exceptions that trigger a retry attempt
    :type Exceptions: Tuple of Exceptions
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    attempt += 1
                    logging.info(
                        f'Exception thrown when attempting to run {func}, attempt {attempt} of {times}'
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def async_retry(times, exceptions):
    """
    Retry Decorator

    :param times: The number of times to repeat the wrapped function/method
    :type times: Int

    :param exceptions: Lists of exceptions that trigger a retry attempt
    :type Exceptions: Tuple of Exceptions
    """

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    # if you want arguments names as a list:
                    args_name = inspect.getfullargspec(func)[0]
                    logging.info(args_name)

                    return await func(*args, **kwargs)
                except exceptions:
                    attempt += 1
                    logging.info(
                        f'Exception thrown when attempting to run {func}, attempt {attempt} of {times}'
                    )
            return await func(*args, **kwargs)

        return wrapper

    return decorator


@retry(times=3, exceptions=(ValueError, TypeError))
def foo1():
    print('Some code here ....')
    print('Oh no, we have exception')
    raise ValueError('Some error')


@async_retry(times=3, exceptions=(ValueError, TypeError))
async def foo2(parm, test=2):
    print('Some code here ....')
    print(f'Oh no, we have exception{parm} {test}')
    raise ValueError('Some error')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [foo2(1, 5)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
