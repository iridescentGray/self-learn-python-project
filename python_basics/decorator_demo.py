import asyncio
import functools
import inspect
import logging
import time
from multiprocessing import RLock
from typing import Callable, Any

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def count_execute_time():
    """
    方法执行时间统计

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
            logging.info(f"methods: {fn.__name__} ,运行共计耗时: {end - start} s")
            return res

        return wrapper

    return wrapper_func


def async_timed(func: Callable) -> Callable:
    """
    协程方法执行时间统计

    Returns:
        装饰器本身

    """

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
    线程安全的单例装饰器
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


def retry(times: int = 3, exceptions=Exception):
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
                except exceptions as e:
                    attempt += 1
                    if attempt < times:
                        logging.error(
                            f"Exception thrown when attempting to run {func}, attempt {attempt} of {times}, error:{e}"
                        )
                    else:
                        logging.exception(
                            f"Exception thrown when attempting to run {func} after {times} attempts, error:{e}"
                        )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def async_retry(times: int = 3, exceptions=Exception):
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
                except exceptions as e:
                    attempt += 1
                    if attempt < times:
                        logging.error(
                            f"Exception thrown when attempting to run {func}, attempt {attempt} of {times}, error:{e}"
                        )
                    else:
                        logging.exception(
                            f"Exception thrown when attempting to run {func} after {times} attempts, error:{e}"
                        )
            return await func(*args, **kwargs)

        return wrapper

    return decorator


def suppress_errors():
    """
    not throw error

    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.exception(f"Error in {func.__name__}: {e}")
                return None

        return wrapper

    return decorator


def log_param_and_result():
    """
    log_param_and_result

    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(
                f"execute {func.__name__} param: - args: {args}, kwargs: {kwargs}"
            )
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} return result: {result}")
            return result

        return wrapper

    return decorator
