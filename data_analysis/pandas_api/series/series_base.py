import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    -Series对象可以用来表示一维数据结构，跟数组非常类似，但是多了一些额外的功能(大量的处理数据的方法)
    -Series的内部结构包含了两个数组，其中一个用来保存数据，另一个用来保存数据的索引
    """
    logging.info(
        f"-----------------------------构建------------------------------------------"
    )
    # 通过列表构建
    ser_by_array = pd.Series(
        data=[320, 180, 300, 405], index=["一季度", "二季度", "三季度", "四季度"]
    )
    logging.info(f" ser_by_array: \n {ser_by_array}")
    # 通过字典构建
    ser_by_dict = pd.Series({"一季度": 320, "二季度": 180, "三季度": 300, "四季度": 405})
    logging.info(f" ser_by_dict: \n {ser_by_dict}")
    logging.info(
        f"-----------------------------访问------------------------------------------"
    )
    # 使用整数索引
    logging.info(
        f"Integer index:\n{ser_by_dict[0]}, {ser_by_dict[2]}, {ser_by_dict[-1]}"
    )
    ser_by_dict[0], ser_by_dict[-1] = 350, 360
    logging.info(f"after change: \n {ser_by_dict}")

    # 使用自定义的标签索引
    logging.info(f"Label Index: \n {ser_by_dict['一季度'], ser_by_dict['三季度']}")
    ser_by_dict["一季度"] = 380
    logging.info(f"Label Index2: \n {ser_by_dict}")
    logging.info(f"Label Index3: \n {ser_by_dict['二季度': '四季度']}")
    # 切片
    ser_by_dict[1:3] = 400, 500
    logging.info(f"after spilt: \n {ser_by_dict}")
    # 花式索引 Fancy index
    logging.info(f"Fancy index \n{ser_by_dict[['二季度', '四季度']]}")
    ser_by_dict[["二季度", "四季度"]] = 500, 520
    logging.info(f"Fancy index after change\n {ser_by_dict[['二季度', '四季度']]}")
    logging.info(
        f"-----------------------------计算------------------------------------------"
    )
    # boolean 索引
    logging.info(f"boolean index: \n {ser_by_dict[ser_by_dict >= 500]}")
    # 求和
    logging.info({ser_by_dict.sum()})
    # 求均值
    logging.info(ser_by_dict.mean())
    # 求最大
    logging.info(ser_by_dict.max())
    # 求最小
    logging.info(ser_by_dict.min())
    # 计数
    logging.info(ser_by_dict.do_count_number())
    # 求标准差
    logging.info(ser_by_dict.std())
    # 求方差
    logging.info(ser_by_dict.var())
    # 求中位数
    logging.info(ser_by_dict.median())
    # 获取上述所有方法的信息
    logging.info(f"describe: \n {ser_by_dict.describe()}")
    logging.info(
        f"-----------------------------去重------------------------------------------"
    )
    ser3 = pd.Series(
        data=["apple", "banana", "apple", "pitaya", "apple", "pitaya", "durian"]
    )
    # 统计每个值重复的次数
    logging.info(f"Value statistics: \n {ser3.value_counts()}")
    # 去重
    logging.info(f"unique: \n {ser3.unique()}")
    # 找出重复项
    logging.info(f"duplicated: \n {ser3.duplicated()}")
    # 移除重复项
    logging.info(f"drop_duplicates: \n {ser3.drop_duplicates()}")
    ser4 = pd.Series(data=[10, 20, np.NaN, 30, np.NaN])
    logging.info(
        f"-----------------------------判断/填充------------------------------------------"
    )
    logging.info(f"isnull: \n {ser4.isnull()}")
    logging.info(f"notnull: \n {ser4.notnull()}")
    # 填充空值
    logging.info(f"fillna: \n {ser4.fillna(value=40)}")
    ser5 = pd.Series(data=[10, 20, np.NaN, 30, np.NaN])
    # 删除空值
    logging.info(f"dropna: \n {ser5.dropna()}")
    # dropna()和fillna()方法都有inplace参数 True修改原Series对象,返回值是None    False(默认)不改原Series对象，返回一个新的Series对象
    ser6 = pd.Series(data=[10, 20, np.NaN, 30, np.NaN])
    ser7 = ser6.fillna(value=40, inplace=False)
    ser8 = ser6.fillna(value=40, inplace=True)
    logging.info(f"fillna inplace param False:\n{ser7}, {ser6 is ser7}")
    logging.info(f"fillna inplace param True:\n{ser8} ,{ser6 is ser8}")
    logging.info(
        f"-----------------------------查找/替换------------------------------------------"
    )
    where_test = pd.Series(range(5))
    # 找出满足条件的项
    logging.info(f"where:\n{where_test}")
    logging.info(f"where find:\n{where_test.where(where_test > 2)}")
    # 把'不满足'条件的项替换为10
    logging.info(f"where replace:\n{where_test.where(where_test > 2, 10)}")
    # 把'满足'条件的项替换为10
    logging.info(f"mask replace:\n{where_test.mask(where_test > 2, 10)}")
    logging.info(
        f"-----------------------------映射/转换------------------------------------------"
    )
    # list映射为series
    ser9 = pd.Series(["cat", "dog", np.nan, "rabbit"])
    logging.info(f"ser9:\n{ser9}")
    # 映射到字符串中
    ser9__format = ser9.map("I am a {}".format, na_action="ignore")
    logging.info(f"ser9__format:\n{ser9__format}")

    # list+index构建series
    ser10 = pd.Series([20, 21, 12], index=["London", "New York", "Helsinki"])
    logging.info(f"ser10:\n{ser10}")
    # 对Series中的所有元素做平方
    ser10_apply_square = ser10.apply(np.square)
    logging.info(f"ser10_apply_square:\n{ser10_apply_square}")
    # 对Series中的所有元素做减法
    ser10_apply_calculation = ser10.apply(lambda x, value: x - value, args=(5,))
    logging.info(f"ser10_apply_calculation:\n{ser10_apply_calculation}")
    logging.info(
        f"-----------------------------排序------------------------------------------"
    )
    # sort_index()/sort_values()方法用于对索引/数据的排序
    # ascending 布尔类型参数,控制升序/降序
    # kind 参数控制排序算法，默认quicksort ,另有mergesort或heapsort
    # na_position 参数控制空值放在最前/最后，默认last
    ser11 = pd.Series(
        data=[35, 96, 12, 57, 25, 89],
        index=["grape", "banana", "pitaya", "apple", "peach", "orange"],
    )
    logging.info(f"sort_values:\n{ser11.sort_values()}")
    logging.info(f"sort_index:\n{ser11.sort_index(ascending=False)}")

    # 找出元素中最大或最小的“Top - N”,不需要进行排序
    # 找出值最大的3个
    logging.info(f"nlargest:\n{ser11.nlargest(3)}")
    # 找出值最小的3个
    logging.info(f"nlargest:\n{ser11.nsmallest(3)}")
