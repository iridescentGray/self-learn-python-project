import logging
import re

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


def func(param):
    print(param)
    print(type(param))
    return param.sum() + param.min()
df2=df.rolling(3).apply(func)

print(df2)