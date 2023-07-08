import random
import string
import time

char_pool = string.ascii_lowercase + string.digits


def long_time_get_str(order):
    """
    order 用于查看方法是否顺序执行
    """
    time.sleep(0.2)
    return f"order is {order} char is {random.choice(char_pool)}"
