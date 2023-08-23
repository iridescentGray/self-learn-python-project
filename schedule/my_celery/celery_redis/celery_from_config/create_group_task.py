from task import add, sub
from celery import group

# 可以调用signature方法，变成一个signature对象
t1 = add.signature(args=(2, 3))
t2 = sub.signature(args=(2, 3))
# 但是变成signature对象之后，我们可以将其当成一个组来执行
gp = group(t1, t2)

# 执行group
res = gp()
print("组id:", res.id)  # 组id: 0eb91aef-ea48-4a6a-bd3e-9cddaa80889e
print("组结果:", res.get())  # 组结果: [5, -1, 6, 2]
