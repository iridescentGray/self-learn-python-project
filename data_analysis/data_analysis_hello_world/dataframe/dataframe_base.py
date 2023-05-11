import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    -DataFrame可以用来表示二维的数据，类似于一个有行有列的表格
    -DataFrame使用最更为广泛
    """
    logging.info(
        f"-----------------------------构建------------------------------------------"
    )
    # 创建随机的10行3列的二维数组
    arrays_scores_data = np.random.randint(60, 101, (10, 3))
    # 列
    courses_columns = ["语文", "数学", "英语"]
    # 行
    arrays_ids_row = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
    # 通过二维数组创建DataFrame对象
    df1 = pd.DataFrame(
        data=arrays_scores_data, columns=courses_columns, index=arrays_ids_row
    )
    logging.info(f"df1: \n{df1}")

    # map的key相当于列 data相当于行
    dict_scores_data = {
        "语文": [62, 72, 93, 88, 93],
        "数学": [95, 65, 86, 66, 87],
        "英语": [66, 75, 82, 69, 82],
    }
    dict_ids_row = [1001, 1002, 1003, 1004, 1005]
    df2 = pd.DataFrame(data=dict_scores_data, index=dict_ids_row)
    logging.info(f"df2: \n{df2}")

    logging.info(
        f"-----------------------------信息------------------------------------------"
    )
    # 直接向控制台打印DataFrame的信息
    logging.info(f"df2.info()")
    df2.info()
    logging.info(f"df2.head() \n{df2.head()}")

    logging.info(f"df2.tail() \n{df2.tail()}")
