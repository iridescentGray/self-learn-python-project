import asyncio
import functools
import inspect
import logging
from datetime import datetime
from multiprocessing import RLock


def count_execute_time(text=""):
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
            logging.info("%s  methods: %s 开始执行" % (text, fn.__name__))
            start = datetime.now()
            res = fn(*args, **kwargs)
            end = datetime.now()
            logging.info(
                "%s  methods: %s ,运行共计耗时: %s s" % (text, fn.__name__, end - start)
            )
            return res

        return wrapper

    return wrapper_func


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
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d' % (func, attempt, times)
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
                    print(args_name)

                    return await func(*args, **kwargs)
                except exceptions:
                    attempt += 1
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d' % (func, attempt, times)
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
