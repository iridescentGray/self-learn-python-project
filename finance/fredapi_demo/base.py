import pandas as pd
from fredapi import Fred

# 初始化 FRED API，替换为你的 API 密钥
fred = Fred(api_key="")

# 获取联邦基金利率数据 (FEDFUNDS)
data = fred.get_series("FEDFUNDS")

# 转换为 Pandas DataFrame
df = pd.DataFrame(data, columns=["Rate"])
df.index.name = "Date"

# 打印最近5条数据
print("最近5条联邦基金利率数据：")
print(df.tail())
