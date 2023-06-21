import logging

import numpy as np
import pandas as pd
import pandas_datareader as pdr

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    -DataFrame是数据分析的主力
    """

    scores = np.random.randint(50, 101, (5, 3))
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    student_df = pd.DataFrame(data=scores, columns=courses, index=names)
    logging.info(f"student_df  \n{student_df}")

    logging.info(
        f"-----------------------------数值分析------------------------------------------"
    )
    # sum()、mean()、std()、var()、min()、max()、argmin()、argmax()、cumsum()
    # 求和、求平均、求标准差、求方差、找最大、找最小、求累积和
    logging.info(f"sum\n {student_df.sum()}")
    # 列平均
    logging.info(f"mean column \n{student_df.mean()}")
    # 行平均
    logging.info(f"mean row\n{student_df.mean(1)}")
    logging.info(f"max  \n{student_df.max()}")
    logging.info(f"min  \n{student_df.min()}")
    logging.info(f"std  \n{student_df.std()}")
    logging.info(f"var  \n{student_df.var()}")
    logging.info(f"cumsum \n{student_df.cumsum()}")
    # 获取上述所有方法的信息
    logging.info(f"describe: \n {student_df.describe()}")

    logging.info(
        f"-----------------------------排序和Top-N------------------------------------------"
    )
    # 按照语文列排序
    logging.info(f"sort by column: \n {student_df.sort_values(by='语文', ascending=False)}")
    # 找出语文列的 前三名
    logging.info(f"top 3 : \n {student_df.nlargest(3, '语文')}")
    logging.info(f"low 3 : \n {student_df.nsmallest(3, '语文')}")

    dataframe_from_excel = pd.read_excel(
        io="file_for_read/2020_sales_data.xlsx"
    )
    logging.info(f"dataframe_from_excel: \n{dataframe_from_excel}")

    logging.info(
        f"-----------------------------追加列-----------------------------------------"
    )
    # 计算销售额 添加到DataFrame中
    dataframe_from_excel['销售额'] = dataframe_from_excel['售价'] * dataframe_from_excel['销售数量']
    logging.info(f"dataframe_from_excel: \n{dataframe_from_excel}")

    logging.info(
        f"----------------------------分组/聚合------------------------------------------"
    )
    #  一级分组,单聚合方式：根据“销售区域”列 对销售额数据进行分组并求和
    logging.info(f"group by field and sum: \n{dataframe_from_excel.groupby('销售区域').销售额.sum()}")
    # 一级分组,单聚合方式,取月份：根据“销售日期”列的月份 对销售额数据进行分组并求和
    logging.info(
        f"group by month and sum: \n{dataframe_from_excel.groupby(dataframe_from_excel['销售日期'].dt.month).销售额.sum()}")
    # 二级分组,单聚合方式,取月份：先根据区域分组 再根据 销售日期 分组
    logging.info(
        f"group by field and sum: \n{dataframe_from_excel.groupby(['销售区域', dataframe_from_excel['销售日期'].dt.month]).销售额.sum()}")
    # 一级分组,一级聚合，多聚合方式：根据'销售区域'分组后,聚合'销售额'
    logging.info(f"agg by: \n{dataframe_from_excel.groupby('销售区域').销售额.agg(['sum', 'max', 'min'])}")
    # 一级分组,一级聚合,多聚合方式,自定义列名：根据'销售区域'分组后,聚合'销售额' 然后自定义聚合后的列名
    logging.info(f"agg: customer\n{dataframe_from_excel.groupby('销售区域').销售额.agg(销售总额='sum', 单笔最高='max', 单笔最低='min')}")
    # 一级分组,多级聚合,多聚合方式：按销售区域分组,统计区域的销售额的平均值 以及销售数量的最低值和最高值
    logging.info(
        f"agg by diff field : \n{dataframe_from_excel.groupby('销售区域')[['销售额', '销售数量']].agg({'销售额': 'mean', '销售数量': ['max', 'min']})}")

    logging.info(
        f"----------------------------透视表------------------------------------------"
    )
    # pivot_table函数中分别对应index和values参数，这两个参数都可以是单个列或者多个列
    # 和groupby的区别：groupby后，如果对单个列进行聚合，得到的结果是一个Series对象，而pivot_table结果是一个DataFrame 对象

    # 简单透视表：
    logging.info(
        f"pivot_table simple field: \n{pd.pivot_table(dataframe_from_excel, index='销售区域', values='销售额', aggfunc='sum')}")

    # 多列透视表： index中的字段会作为列
    logging.info(
        f"pivot_table mut line: \n{pd.pivot_table(dataframe_from_excel, index=['销售区域', dataframe_from_excel['销售日期'].dt.month], values='销售额', aggfunc='sum')}")

    # 多行透视表：columns中的字段会作为行
    # fill_value=0会将空值处理为0。
    logging.info(
        f"pivot_table mut row: \n{pd.pivot_table(dataframe_from_excel, index='销售区域', columns=dataframe_from_excel['销售日期'].dt.month, values='销售额', aggfunc='sum', fill_value=0)}")

    # 多行透视表：处理数据，以添加行
    dataframe_from_excel['月份'] = dataframe_from_excel['销售日期'].dt.month
    # 多行透视表：添加聚合列
    # margins：对行数据进行聚合，margins_name: 聚合结果列名
    logging.info(
        f"pivot_table add aggregate Column: \n{pd.pivot_table(dataframe_from_excel, index='销售区域', columns='月份', values='销售额', aggfunc='sum', fill_value=0, margins=True, margins_name='总计')}")

    logging.info(
        f"----------------------------交叉表------------------------------------------"
    )
    sales_area, sales_month, sales_amount = dataframe_from_excel['销售区域'], dataframe_from_excel['月份'], \
                                            dataframe_from_excel['销售额']
    logging.info(
        f"cross tab: \n{pd.crosstab(index=sales_area, columns=sales_month, values=sales_amount, aggfunc='sum').fillna(0).applymap(int)}")

    logging.info(
        f"----------------------------窗口/滑动/采样------------------------------------------"
    )
    # rolling方法可以将数据置于窗口中，然后就可以使用函数对窗口中的数据进行运算和处理
    # count()	统计非空数量
    # sum()	求和
    # mean()	求均值
    # median()	求中位数
    # min()	最小值
    # max()	最大值
    # std()	求标准差
    # var()	有偏方差
    # skew()	偏度
    # kurt()	峰度
    # quantile()	求四分位数
    # apply()	apply函数使用
    # cov()	无偏方差
    # corr()	相关系数

    # 获取baidu的股票数据
    baidu_df = pdr.get_data_stooq('BIDU', start='2021-11-22', end='2021-12-7')
    baidu_df.sort_index(inplace=True)
    logging.info(f"baidu df: \n{baidu_df}")
    # 5日均线
    logging.info(f"baidu df rolling 5: \n{baidu_df.rolling(5).mean()}")
    # Close的7日均线
    logging.info(f"baidu df Close field rolling: \n{baidu_df.Close.rolling(7).mean()}")

    # shift()方法：通过时间前移或后移数据
    logging.info(f"baidu df shift 2: \n{baidu_df.shift(2, fill_value=0)}")
    logging.info(f"baidu df shift -2: \n{baidu_df.shift(-2, fill_value=0)}")
    # asfreq() 指定一个时间频率抽取对应的数据
    logging.info(f"baidu df asfreq('5D'): \n{baidu_df.asfreq('5D')}")
    # 基于时间对数据进行重采样，相当于根据时间周期对数据进行了分组操作
    logging.info(f"baidu df resample('1M'): \n{baidu_df.resample('1M').mean()}")

    logging.info(
        f"----------------------------协方差/相关系数------------------------------------------"
    )
    # ·协方差（covariance）来衡量两个随机变量的联合变化程度，显示两个变量的相关性。
    # 1.如果变量 X 的较大值主要与变量 Y 的较大值相对应，而两者较小值也相对应，那么两个变量倾向于表现出相似的行为，协方差为正
    # 2.如果变量 X 的较大值主要对应于变量 Y 的较小值，则两个变量倾向于表现出相反的行为，协方差为负
    # 3.如果X和Y是统计独立的，那么二者的协方差为0
    # ·'皮尔逊积矩相关系数'就是正态形式的协方差，它用于度量两个变量间的相关程度（线性相关），其值介于-1到1之间，皮尔逊相关系数适用于：
    # 1.两个变量之间是线性关系，都是连续数据
    # 2.两个变量的总体是正态分布，或接近正态的单峰分布
    # 3.两个变量的观测值是成对的，每对观测值之间相互独立
    boston_df = pd.read_csv('file_for_read/boston_house_price.csv')
    # DataFrame对象的cov方法和corr方法分别用于计算协方差和相关系数
    # corr方法的第一个参数method的默认值是pearson，表示计算皮尔逊相关系数
    logging.info(f"boston_df Pearson: \n{boston_df.corr()}")
    # ；还可以指定kendall或spearman来获得肯德尔系数或斯皮尔曼等级相关系数。
    logging.info(f"boston_df spearman: \n{boston_df.corr('spearman')}")
