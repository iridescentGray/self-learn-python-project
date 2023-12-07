import logging

import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # 创建随机的三维数组
    three_dimensional_array = np.random.randint(1, 100, (3, 4, 5))
    logging.info(f" three_dimensional_array: {three_dimensional_array}")

    # 读取图片获得对应的三维数组
    # 每个像素点是由红绿蓝三原色构成的，所以能够用三维数组来表示
    image_three_dimensional_array = plt.imread("test.png")
    logging.info(f" image_three_dimensional_array: {image_three_dimensional_array}")
