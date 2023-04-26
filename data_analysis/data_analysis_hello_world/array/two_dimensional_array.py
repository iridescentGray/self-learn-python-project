import logging

import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    """
    二维数组
    """
    # 嵌套两个array，组成一个二维数组
    two_dimensional_array1 = np.array([[1, 2, 3], [4, 5, 6]])
    logging.info(f" two_dimensional_array1: {two_dimensional_array1}")
    two_dimensional_array2 = np.zeros((3, 4))
    logging.info(f" two_dimensional_array2: {two_dimensional_array2}")

    # 创建全是0的二维数组
    two_dimensional_zero_array = np.zeros((3, 4))
    logging.info(f" two_dimensional_zero_array: {two_dimensional_zero_array}")

    # 创建全是1的二维数组
    two_dimensional_ones_array = np.ones((3, 4))
    logging.info(f" two_dimensional_ones_array: {two_dimensional_ones_array}")

    # 创建满二维数组
    two_dimensional_full_array = np.full((3, 4), 10)
    logging.info(f" two_dimensional_full_array: {two_dimensional_full_array}")

    # 将一维数组变成二维数组
    one_dimensional_to_two_dimensional_array = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
    logging.info(f" one_dimensional_to_two_dimensional_array: {one_dimensional_to_two_dimensional_array}")

    # 产生$[0, 1)$范围的随机小数构成的3行4列的二维数组
    random_two_dimensional_array = np.random.rand(3, 4)
    logging.info(f" random_two_dimensional_array: {random_two_dimensional_array}")

    # $[1, 100)$范围的随机整数构成的3行4列的二维数组
    random_int_two_dimensional_array = np.random.randint(1, 100, (3, 4))
    logging.info(f" random_int_two_dimensional_array: {random_int_two_dimensional_array}")
