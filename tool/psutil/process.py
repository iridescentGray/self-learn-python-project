import datetime
from pprint import pprint

import psutil

print("----------------------------pids------------------------------")
"""
查看当前存在的所有进程的 pid

"""
pprint(psutil.pids())

print("----------------------------pid_exists------------------------------")
# 查看某个进程是否存在
pprint(psutil.pid_exists(22333))  # False
pprint(psutil.pid_exists(0))

print("----------------------------get Process------------------------------")
# 根据 pid 获取一个进程对应的 Process 对象
pprint(psutil.Process(pid=0))

print("----------------------------get Process Detail------------------------------")
p = psutil.Process(pid=1212)
# 进程名称
print(p.name())
# 进程的exe路径
print(p.exe())
# 进程的工作目录
print(p.cwd())
# 进程启动的命令行
print(p.cmdline())
# 当前进程id
print(p.pid)
# 父进程id
print(p.ppid())
# 父进程
print(p.parent())
# 子进程列表
pprint(p.children())
# 进程状态
print(p.status())
# 进程用户名
print(p.username())
# 进程创建时间戳
print(p.create_time())
# 进程使用的cpu时间
print(p.cpu_times())
# 进程所使用的的内存
print(p.memory_info())
print(
    "----------------------------get Process Detail Files------------------------------"
)

# 进程打开的文件
pprint(p.open_files())
print(
    "----------------------------get Process Detail connections------------------------------"
)

# 进程相关的网络连接
pprint(p.connections())
print(
    "----------------------------get Process Detail Thread------------------------------"
)
print(p.num_threads())
# pprint(p.threads())

print(
    "----------------------------get Process Detail environ------------------------------"
)
pprint(p.environ())

print("----------------------------process_iter------------------------------")
# 返回所有进程（Process）对象组成的迭代器
pprint(psutil.process_iter())

for prcs in psutil.process_iter():
    if prcs.name().lower() == "wechat":
        print(prcs.pid)
