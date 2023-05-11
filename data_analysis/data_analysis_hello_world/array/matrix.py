import logging

import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    矩阵
    官方并不推荐使用matrix类而是建议使用二维数组，而且有可能在将来的版本中会移除matrix类
    """
    # 创建单位矩阵
    identity_matrix = np.eye(4)
    logging.info(f" identity_matrix: {identity_matrix}")
    matrix1 = np.matrix("1 2 3; 4 5 6")
    logging.info(f" matrix1: {matrix1}")

    matrix2 = np.asmatrix(np.array([[1, 1], [2, 2], [3, 3]]))
    logging.info(f" matrix2: {matrix2}")

    # 获取矩阵对象对应的ndarray对象
    logging.info(f" matrix2 inner array: {matrix2.A}")
    # 获取矩阵对象对应的扁平化后的对象
    logging.info(f" matrix2 A1: {matrix2.A1}")
    # 可逆矩阵的逆矩阵
    logging.info(f" Inverse matrix: {matrix2.I}")
    # 矩阵的转置
    logging.info(f" matrix Transposition: {matrix2.T}")
    logging.info(f" matrix shape: {matrix2.shape}")
    logging.info(f" matrix size: {matrix2.size}")
