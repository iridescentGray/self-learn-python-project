import psutil

"""
查看内存使用情况

total: 总内存
available: 可用内存
percent: 内存使用率
used: 已使用的内存
"""
print(psutil.virtual_memory())

# 查看交换内存信息
print(psutil.swap_memory())
