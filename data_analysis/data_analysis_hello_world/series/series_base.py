import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # 通过列表构建
    ser_by_array = pd.Series(data=[320, 180, 300, 405], index=['一季度', '二季度', '三季度', '四季度'])
    logging.info(f" ser_by_array: {ser_by_array}")
    # 通过字典构建
    ser_by_dict = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})
    logging.info(f" ser_by_dict: {ser_by_dict}")
    # 使用整数索引
    logging.info(f"Integer index:{ser_by_dict[0]}, {ser_by_dict[2]}, {ser_by_dict[-1]}")
    ser_by_dict[0], ser_by_dict[-1] = 350, 360
    logging.info(f"after change: {ser_by_dict}")

    # 使用自定义的标签索引
    logging.info(f"Label Index: {ser_by_dict['一季度'], ser_by_dict['三季度']}")
    ser_by_dict['一季度'] = 380
    logging.info(f"Label Index2: {ser_by_dict}")
    logging.info(f"Label Index3: {ser_by_dict['二季度': '四季度']}")

    # 切片
    ser_by_dict[1:3] = 400, 500
    logging.info(f"after spilt: {ser_by_dict}")
    # 花式索引 Fancy index
    logging.info(f"Fancy index {ser_by_dict[['二季度', '四季度']]}")
    ser_by_dict[['二季度', '四季度']] = 500, 520
    logging.info(f"Fancy index after change {ser_by_dict[['二季度', '四季度']]}")

    # boolean 索引
    logging.info(f"boolean index: {ser_by_dict[ser_by_dict >= 500]}")
    # 求和
    logging.info({ser_by_dict.sum()})
    # 求均值
    logging.info(ser_by_dict.mean())
    # 求最大
    logging.info(ser_by_dict.max())
    # 求最小
    logging.info(ser_by_dict.min())
    # 计数
    logging.info(ser_by_dict.count())
    # 求标准差
    logging.info(ser_by_dict.std())
    # 求方差
    logging.info(ser_by_dict.var())
    # 求中位数
    logging.info(ser_by_dict.median())
    # 获取上述所有方法的信息
    logging.info(f"describe: {ser_by_dict.describe()}")

    ser3 = pd.Series(data=['apple', 'banana', 'apple', 'pitaya', 'apple', 'pitaya', 'durian'])
    # 统计每个值重复的次数
    logging.info(f"Value statistics: {ser3.value_counts()}")
    # 去重
    logging.info(f"unique: {ser3.unique()}")


    ser4 = pd.Series(data=[10, 20, np.NaN, 30, np.NaN])
    # dropna() 和fillna()方法分别用来删除空值和填充空值
    ser4.dropna()
    ser4.fillna(value=40)
    ser4.fillna(method='ffill')
