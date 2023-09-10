import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)


"""
-DataFrame rolling函数
"""
logging.info("---------------init datasource---------------")
df = pd.DataFrame(
    {"col1": list(range(10)), "col2": list(range(1, 11)), "col3": list(range(3, 13))}
)
print(df)
logging.info("---------------type of rolling --------------")
print(type(df.rolling(3)))  # <class 'pandas.core.window.rolling.Rolling'>

logging.info("-----------rolling(3).sum()-------------------")
# 使用sum滚动求和
print(df.rolling(3).sum())

logging.info("-----------rolling(3).agg-------------------")
# 使用agg滚动求和
print(df.rolling(3).agg(lambda x: sum(x)))

logging.info("-----------rolling(3).agg with different fun-------------------")
# 传递一个字典, 将不同的函数应用在不同的列
print(df.rolling(3).agg({"col1": "sum", "col2": "mean", "col3": "min"}))


logging.info("-----------rolling(3) step=2-------------------")
# step=2 把rolling的计算结果分步切片
# sum的结果和rolling一致，单纯但少了一些数据，少了的这些数据不影响计算
rolling_step = df.rolling(3, step=2).sum()
print(rolling_step)



