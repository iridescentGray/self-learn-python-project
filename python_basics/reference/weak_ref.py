import weakref

"""
测试弱引用
"""


class SimpleObject:
    def __del__(self):
        print("SimpleObject __del__")


strong_ref = SimpleObject()
weak_ref = weakref.ref(strong_ref)
print(f"strong_ref: {strong_ref}")
print(f"weak_ref:  {weak_ref}")
print(f"weak_ref() is strong_ref: {weak_ref() is strong_ref}")
del strong_ref  # 删除 obj 会执行SimpleObject的析构函数
print("weak_ref():", weak_ref())  # r(): None
# 打印弱引用, 告诉我们状态已经变成了 dead
print(weak_ref)
