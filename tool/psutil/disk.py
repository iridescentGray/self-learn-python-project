from pprint import pprint

import psutil

print("----------------------------disk_partitions------------------------------")

# 查看磁盘分区、磁盘使用率和磁盘 IO 信息
pprint(psutil.disk_partitions())

print("----------------------------disk_usage-----------------------------------")
print(psutil.disk_usage("/dev/disk1s3"))

print("----------------------------disk_io_counters-----------------------------------")
pprint(psutil.disk_io_counters())

#  perdisk=True，代表分别列出每一个磁盘的统计信息
pprint(psutil.disk_io_counters(perdisk=True))
