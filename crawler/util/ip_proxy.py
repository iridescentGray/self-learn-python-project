# -*- coding:UTF-8 -*-
import random
import re
import subprocess as sp


def init_re_pattern():
    """
    函数说明:初始化正则表达式
    Parameters:

    Returns:
        lose_time - 匹配丢包数
        waste_time - 匹配平均时间
    Modify:
        2017-05-27
    """
    # 匹配丢包数
    success_received = re.compile("(\d+) packets received", re.IGNORECASE)
    # 匹配平均时间
    waste_time = re.compile("time=(\d+)ms", re.IGNORECASE)
    return success_received, waste_time


def get_proxy_list():
    """
    函数说明:获取IP代理
    Parameters:
        page - 获取第一页
    Returns:
        proxys_list - 代理列表
    Modify:
        2017-05-27
    """

    # 存储代理的列表
    proxys_list = []
    proxys_list.append("127.0.0.1")
    # 返回代理列表
    return proxys_list


def check_ip(need_check_ip, success_received, waste_time):
    """
    函数说明:检查代理IP的连通性
    Parameters:
        ip - 代理的ip地址
        lose_time - 匹配丢包数
        waste_time - 匹配平均时间
    Returns:
        average_time - 代理ip平均耗时
    Modify:
        2017-05-27
    """
    # 命令 -c 要发送的回显请求数 -i 等待每次回复的超时时间(毫秒)
    cmd = "ping -c3 -i1 %s"
    # 执行命令
    p = sp.Popen(
        cmd % need_check_ip, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True
    )
    # 获得返回结果并解码
    out = p.stdout.read().decode("utf-8")
    # 丢包数
    success_received = success_received.findall(out)
    if len(success_received) == 3:
        return True
    else:
        return False


def get_effective_ip(ip_list: list):
    success_received, waste_time = init_re_pattern()
    # 如果平均时间超过200ms重新选取ip
    while ip_list:
        # 从100个IP中随机选取一个IP作为代理进行访问
        ip = random.choice(ip_list)

        # 检查ip
        can_use = check_ip(ip, success_received, waste_time)
        if can_use:
            ip_list.remove(ip)
            print("ip 连接超时, 重新获取中!")
        else:
            return ip


if __name__ == "__main__":
    # 获取IP代理
    proxy_list = get_proxy_list()
    proxy_ip = get_effective_ip(proxy_list)
    print("使用代理:", proxy_ip)
