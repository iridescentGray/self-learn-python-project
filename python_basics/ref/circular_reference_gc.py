"""
测试循环依赖GC
"""


import gc
import time


class A:
    def __init__(self, obj):
        self.obj = obj

    def __del__(self):
        print("当实例对象被回收时, 会触发我的执行······")


a = A(123)
b = A(123)

a.obj = b
b.obj = a

del a, b
# 主动触发gc,发动之后会找出发生循环引用的对象并回收
gc.collect()  # 尝试注释这段代码，以观察变化


time.sleep(3)
