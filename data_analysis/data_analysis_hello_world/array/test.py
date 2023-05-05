# -*- coding: utf-8 -*-
import time
from functools import update_wrapper


class DelayedStart:
    """在执行被装饰函数前，等待 1 秒钟"""

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Wait for 1 second before starting...')
        time.sleep(1)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        """跳过等待，立刻执行被装饰函数"""
        print('Call without delay')
        return self.func(*args, **kwargs)


@DelayedStart
def hello():
    print("Hello, World.")


if __name__ == '__main__':
    hello()  # 使用装饰器
    hello.eager_call()  # 执行由装饰器类提供的方法
