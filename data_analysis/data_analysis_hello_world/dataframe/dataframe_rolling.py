import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)


"""
-DataFrame rolling函数
"""
logging.info(
    "------------------------------"
)

amount = pd.Series([100, 90, 110, 150, 110, 130, 80, 90, 100, 150])
print(amount.rolling(3).sum())
