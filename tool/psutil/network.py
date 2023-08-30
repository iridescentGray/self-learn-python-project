from pprint import pprint
import psutil

print("----------------------------net_io_counters------------------------------")

"""
查看网卡的网络 IO 统计信息
bytes_sent: 发送的字节数
bytes_recv: 接收的字节数
packets_sent: 发送的包数据量
packets_recv: 接收的包数据量
errin: 接收包时, 出错的次数
errout: 发送包时, 出错的次数
dropin: 接收包时, 丢弃的次数
dropout: 发送包时, 丢弃的次数
"""
pprint(psutil.net_io_counters())
print("----------------------------net_io_counters pernic=True------------------------------")

pprint(psutil.net_io_counters(pernic=True))

print("------------------------------------------net_if_addrs-------------------------------------")

# 以字典的形式返回网卡的配置信息, 包括 IP 地址、Mac地址、子网掩码、广播地址等等
pprint(psutil.net_if_addrs())
print("------------------------------------------net_if_stats-------------------------------------")

# 返回网卡的详细信息, 包括是否启动、通信类型、传输速度、mtu
pprint(psutil.net_if_stats())

print("------------------------------------------net_connections-------------------------------------")

# 查看当前机器的网络连接
# pprint(psutil.net_connections())

pprint(psutil.users())  






