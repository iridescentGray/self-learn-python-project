import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)


"""
-DataFrame FQA环节
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


def change_dataframe_data(dataframe: pd.DataFrame):
    dataframe.loc[(dataframe["语文"] > 90), "is_more_than_90"] = 1
    pass


change_dataframe_data(df1)
logging.info(f"被在方法内部修改,增加is_more_than_90这一列: \n{df1}")

