import logging

import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    NumPy中的数学运算和数学函数会自动作用于数组中的每个成员（不用循环遍历）
    """
    # 生成随机数创建数组对象,产生10个$[0, 1)$范围的随机小数
    random_rand_array = np.arange(1, 10)
    # 全部乘10
    logging.info(f"multiplication {random_rand_array * 10}")

    random_rand_array2 = np.arange(1, 10)
    # 二维数组相加
    logging.info(f"array add {random_rand_array +random_rand_array2}")
