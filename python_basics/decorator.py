import functools
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
            logging.info("%s  methods: %s ,运行共计耗时: %s s" % (text, fn.__name__, end - start))
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
