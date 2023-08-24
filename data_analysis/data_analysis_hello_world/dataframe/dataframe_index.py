import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    -DataFrame可以用来表示二维的数据,类似于一个有行有列的表格
    -DataFrame使用最更为广泛
    """
    logging.info(
        "-----------------------------构建------------------------------------------"
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
    row_1004 = df1.loc[1004]["语文"]
    logging.info(f"df1 row_1004.语文: \n{row_1004}")

    row_1004 = df1.loc[1004].语文
    logging.info(f"df1 row_1004.语文: \n{row_1004}")

    df1_tail = df1.tail(1)
    logging.info(f"df1_tail type: \n{type(df1_tail)}")
    # 使用tail获取最后一行的index
    logging.info(f"df1_tail index[0]: \n{df1_tail.index[0]}")
    # 使用tail获取最后一行,然后获取一列的值
    logging.info(f"df1_tail get line value: \n{df1_tail['语文'].values[0]}")

    # 获取语文最高分的index
    highest_chinese_score_index = df1["语文"].idxmax()
    logging.info(f"highest_chinese_score_index: \n{highest_chinese_score_index}")

    # 找到语文分数等于97的学生所在行的索引的具体数字部分
    chinese_97_index_numbers = df1[df1["语文"] == 97].index.tolist()
    logging.info(f"chinese_97_index_numbers: \n{chinese_97_index_numbers}")
