import logging

import numpy as np
import pandas as pd


logging.basicConfig(level=logging.INFO)


"""
-DataFrame 迭代
"""
logging.info(
    "----------Dataframe 作为参数被传递时,修改参数dataframe会影响原本的Dataframe吗? 会--------------------"
)

df1 = pd.DataFrame(
    data=np.random.randint(60, 101, (10, 3)),
    columns=["语文", "数学", "英语"],
    index=np.random.randint(1, 101, size=10),
)

logging.info(f"df1: \n{df1}")


for index, row in df1.iterrows():
    ratio_value = row['语文']
    print(f"行 {index} {type(index)} 的 ratio 语文: {ratio_value}")
    