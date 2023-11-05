"""
测试引用计数
"""


class A:
    def __init__(self, obj):
        self.obj = obj

    def __del__(self):
        print("当实例对象被回收时, 会触发我的执行······")


# 显然我们创建了一个对象 A(123), 然后让变量 a 指向（引用）它
# 然后 b = a, 让 b 也指向 a 指向的对象
a = A(123)
b = a

del a
print("无事发生, 一切正常")

del b
print("触发完__del__函数, 这里会打印")
