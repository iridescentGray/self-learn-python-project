import logging

import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    simple_array = np.array([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
    # sum()、mean()、std()、var()、min()、max()、argmin()、argmax()、cumsum()
    # 求和、求平均、求标准差、求方差、找最大、找最小、求累积和
    logging.info(f'sum {simple_array.sum()}')
    logging.info(f'mean {simple_array.mean()}')
    logging.info(f'max {simple_array.max()}')
    logging.info(f'min {simple_array.min()}')
    logging.info(f'std {simple_array.std()}')
    logging.info(f'var {simple_array.var()}')
    logging.info(f'cumsum {simple_array.cumsum()}')

    # 序列化
    simple_array.dump('simple_array-data')
    simple_array_load = np.load('simple_array-data', allow_pickle=True)
    print(simple_array_load)

    # fill() 向数组中填充指定的元素。
    # flatten() 将多维数组扁平化为一维数组。
    # nonzero() 方法：返回非0元素的索引。
    # round() 方法：对数组中的元素做四舍五入操作。
    # astype()方法：拷贝数组，并将数组中的元素转换为指定的类型。
    # sort() 方法：对数组进行就地排序。

    # swapaxes()和transpose()方法：交换数组指定的轴。
    two_dimensional_array1 = np.array([[1, 2, 3], [4, 5, 6]])
    # 对于二维数组，transpose相当于实现了矩阵的转置
    transpose = two_dimensional_array1.transpose()
    swapaxes = two_dimensional_array1.swapaxes(0, 1)
    logging.info(f'two_dimensional_array1 transpose {transpose}')
    logging.info(f'two_dimensional_array1 swapaxes {swapaxes}')
