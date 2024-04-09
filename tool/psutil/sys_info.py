import datetime
from pprint import pprint

import psutil

print("----------------------------users------------------------------")
"""
查看当前登录的用户信息

name: 用户名
terminal: 终端
host: 主机地址
started: 登录时间
pid: 进程id
"""
pprint(psutil.users())

print("----------------------------boot_time------------------------------")
# 查看系统的启动时间
pprint(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()))
