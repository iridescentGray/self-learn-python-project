import logging

import matplotlib.pyplot as plt
import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    -使用DataFrame画图,DataFrame对象提供了plot方法来支持绘图，底层仍然是通过matplotlib库实现图表的渲染
    """

    dataframe_from_excel = pd.read_excel(
        io="file_for_read/2020_sales_data.xlsx"
    )
    dataframe_from_excel['销售额'] = dataframe_from_excel['售价'] * dataframe_from_excel['销售数量']
    logging.info(f"dataframe_from_excel: \n{dataframe_from_excel}")
    logging.info(
        f"----------------------------画图------------------------------------------"
    )
    plt.rcParams["font.sans-serif"] = ["SimHei", "Songti SC", "STFangsong"]

    sales_revenue = pd.pivot_table(dataframe_from_excel, index='销售区域', values='销售额', aggfunc='sum')
    # 柱状图
    sales_revenue.plot(figsize=(8, 4), kind='bar')
    # 将横轴刻度上的文字旋转到0度
    plt.xticks(rotation=0)

    # 饼状图
    pd.pivot_table(dataframe_from_excel, index='销售区域', values='销售额', aggfunc='sum') \
        .sort_values(by='销售额', ascending=False) \
        .plot(figsize=(6, 6), kind='pie', y='销售额', autopct='%.2f%%', pctdistance=0.8,
              wedgeprops=dict(linewidth=1, width=0.35))

    plt.legend(loc='center')
    plt.show()
