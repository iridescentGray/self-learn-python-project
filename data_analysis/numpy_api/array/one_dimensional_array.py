import logging

import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # 生成随机数创建数组对象,产生10个$[0, 1)$范围的随机小数
    random_rand_array = np.random.rand(10)
    logging.info(f" random_rand_array: {random_rand_array}")

    # 产生10个$[1, 100)$范围的随机整数
    randint_list = np.random.randint(1, 100, 10)
    logging.info(f" np.random.randint: {randint_list}")

    # 产生10个“标准正态”分布随机数
    randn_list = np.random.randn(10)
    logging.info(f" randn_list: {randn_list}")

    # 产生20个$\mu=50$，$\sigma=10$的正态分布随机数
    random_normal_list = np.random.normal(50, 10, 20)
    logging.info(f" random_normal_list: {random_normal_list}")

    # 使用array函数，通过list创建数组对象
    simple_array = np.array([1, 2, 3, 4, 5])
    logging.info(f" simple_array: {simple_array}")

    # 使用arange函数，指定取值范围创建数组对象
    range_array = np.arange(0, 20, 2)
    logging.info(f" arange: {range_array}")

    # 用指定范围均匀间隔的数字创建数组对象
    linspace_array = np.linspace(-5, 5, 101)
    logging.info(f" linspace_array: {linspace_array}")
