import logging

import numpy as np
import pandas as pd

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
        f"----------------------------透视表和交叉表------------------------------------------"
    )
    # pivot_table函数中分别对应index和values参数，这两个参数都可以是单个列或者多个列
    # groupby操作后，如果对单个列进行聚合，得到的结果是一个Series对象，而pivot_table结果是一个DataFrame 对象
    logging.info(
        f"pivot_table single field: \n{pd.pivot_table(dataframe_from_excel, index='销售区域', values='销售额', aggfunc='sum')}")
    logging.info(
        f"pivot_table mut field : \n{pd.pivot_table(dataframe_from_excel, index='销售区域', columns=dataframe_from_excel['销售日期'].dt.month,values='销售额', aggfunc='sum', fill_value=0)}")
