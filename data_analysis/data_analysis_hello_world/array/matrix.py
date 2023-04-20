import logging

import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    """
    矩阵
    """
    # 创建单位矩阵
    identity_matrix = np.eye(4)
    logging.info(f" identity_matrix: {identity_matrix}")
