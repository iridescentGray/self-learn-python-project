from celery import chain
from task import add

# 整个过程等价于[2+3+3+10]=18
my_chain = chain(
    add.signature(args=(2, 3)) | add.signature(args=(3,)) | add.signature(args=(10,))
)


# 执行chain
res = my_chain()
# 获取最终返回值
print(res.get())  # 128
