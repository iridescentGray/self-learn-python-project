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
    df1.info()
    logging.info(f"df1: \n{df1}")

    # 通过dict构建，map的key相当于列 data相当于行
    dict_scores_data = {
        "语文": [62, 72, 93, 88, 93],
        "数学": [95, 65, 86, 66, 87],
        "英语": [66, 75, 82, 69, 82],
    }
    dict_ids_row = [1011, 1012, 1013, 1014, 1015]
    df2 = pd.DataFrame(data=dict_scores_data, index=dict_ids_row)
    logging.info(f"df2: \n{df2}")


    logging.info(
        "-----------------------------访问------------------------------------------"
    )
    # 根据列名，获取列
    logging.info(f"df1-columns-by-index: \n{df1.语文}")
    # 类似dict一样，获取单列
    logging.info(f"df1-columns-name: \n{df1['语文']}")
    # 获取到的列，其实是Series
    logging.info(f"df1-columns-type is Series: \n{type(df1.语文)}")
    # 获取多列
    logging.info(f"df1-mut-columns-name: \n{df1[['语文', '数学']]}")

    # 根据下标，获取一行
    logging.info(f"df1-row-by-index: \n{df1.iloc[0]}")
    # 根据行名，获取一行
    logging.info(f"df1-row-name: \n{df1.loc[1001]}")
    # 根据行名和列名，获取行列对应的数据
    logging.info(f"df1-row-columns-name: \n{df1.loc[1001].语文}")
    # 获取多列
    logging.info(f"df1-mut-row-name: \n{df1.loc[[1001, 1002]]}")
    # 修改某行某列的数据
    df1.loc[1001, "英语"] = 9999
    logging.info(f"df1-modify-data: \n{df1}")

    # head和tail，查看DataFrame的头部或尾部的数据，默认参数是5
    logging.info(f"df1.head() \n{df1.head()}")
    logging.info(f"df1.tail() \n{df1.tail()}")

    logging.info(
        "-----------------------------筛选------------------------------------------"
    )
    # 列出英语大于90分的
    logging.info(f"df1 over 90 points: \n{df1[df1.英语 > 90]}")
    logging.info(f"df1 query over 90 points: \n{df1.query('英语>90')}")

    logging.info(
        "-----------------------------拼接/合并------------------------------------------"
    )
    # 将两个DataFrame拼接
    logging.info(f" after concat: \n{ pd.concat([df1, df2])}")
    logging.info(f"after left merge: \n{ pd.merge(df1, df2, how='left')}")
    logging.info(f"after right merge: \n{ pd.merge(df1, df2, how='right')}")
    logging.info(f"after inner merge: \n{ pd.merge(df1, df2, how='inner')}")
    # 指定key的合并
    logging.info(
        f"after left merge by idx: \n{ pd.merge(df1, df2, how='left',on='语文')}"
    )
