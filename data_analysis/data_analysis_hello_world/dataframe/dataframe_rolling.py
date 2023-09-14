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



logging.info("-----------rolling(2) shift-------------------")

data = {'values': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# 将数据向前移动一个位置
df['shifted_values'] = df['values'].shift(1)
print(df)
rolling_sum = df['shifted_values'].rolling(window=2).sum()
print(rolling_sum)



logging.info("-----------rolling(2) max.min------------------")

np.random.seed(0)
data = {'open': np.random.rand(30),
        'close': np.random.rand(30)}
df = pd.DataFrame(data)

# 使用 rolling 计算前 250 根 open 和 close 的最大值
rolling_max_open = df['open'].shift(1).rolling(window=4).max()
rolling_max_close = df['close'].shift(1).rolling(window=4).max()
rolling_min_open = df['open'].shift(1).rolling(window=4).min()
rolling_min_close = df['close'].shift(1).rolling(window=4).min()


# 合并结果为一个新的列 max_price

df['max_price'] = pd.concat([rolling_max_open, rolling_max_close], axis=1).max(axis=1)
df['min_price'] = pd.concat([rolling_min_open, rolling_min_close], axis=1).min(axis=1)

print(df)
