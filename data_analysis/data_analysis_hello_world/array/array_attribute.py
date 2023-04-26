import logging

import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # 随机的的三维数组
    three_dimensional_array = np.random.randint(1, 100, (3, 4, 5))
    logging.info(f" three_dimensional_array: {three_dimensional_array}")
    # 数组的形状
    logging.info(f" three_dimensional_array.shape : {three_dimensional_array.shape}")
    # 数组数据类型
    logging.info(f" three_dimensional_array.dtype : {three_dimensional_array.dtype}")
    # 大小
    logging.info(f" three_dimensional_array.size : {three_dimensional_array.size}")
    # 数组维度
    logging.info(f" three_dimensional_array.ndim : {three_dimensional_array.ndim}")
    # 数组单元素占用内存空间字节
    logging.info(f" three_dimensional_array.itemsize : {three_dimensional_array.itemsize}")
    # 数组数组所有元素占用内存空间字节
    logging.info(f" three_dimensional_array.nbytes : {three_dimensional_array.nbytes}")