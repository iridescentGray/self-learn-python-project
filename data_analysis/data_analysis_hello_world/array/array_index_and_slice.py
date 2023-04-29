import logging

import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # 随机的的三维数组
    three_dimensional_array = np.random.randint(1, 100, (3, 4, 5))

    # 切片后得到的新的数组section的base属性就是three_dimensional_array
    three_dimensional_array_slice = three_dimensional_array[:]
    logging.info(f" three_dimensional_array_slice.base : {three_dimensional_array_slice.base is three_dimensional_array}")
    logging.info(f" three_dimensional_array_slice : {three_dimensional_array_slice is three_dimensional_array}")