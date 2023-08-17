import os
import time


print(os.times())
# nt.times_result(user=0.09375, system=0.109375, children_user=0.0, children_system=0.0, elapsed=0.0)

"""
user：用户时间s
system：系统时间
children_user：所有子进程的用户时间
children_system：所有子进程的系统时间
elapsed：子过去的固定点以来经过的实际时间
"""
print(os.times().user)  # 0.09375