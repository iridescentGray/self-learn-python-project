import psutil

# 获取 CPU 的逻辑核心数量
print(psutil.cpu_count())

# 获取 CPU 的物理核心数量
print(psutil.cpu_count(logical=False))

# 统计 CPU 的用户／系统／空闲时间
print(psutil.cpu_times())

# 查看 CPU 的使用率
for x in range(3):
    # interval：表示每隔0.5s刷新一次
    # percpu：表示查看所有的cpu使用率
    print(psutil.cpu_percent(interval=0.5, percpu=True))  # cpu的逻辑数有多少, 列表里面就有多少个元素


# 查看 CPU 的统计信息，包括上下文切换、中断、软中断，以及系统调用次数等等
print(psutil.cpu_stats())
