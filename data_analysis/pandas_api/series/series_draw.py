import logging

import matplotlib.pyplot as plt
import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    -Series对象有一个名为plot的方法可以用来生成图表，如果选择生成折线图、饼图、柱状图等
    -默认会使用Series对象的索引作为横坐标，使用Series对象的数据作为纵坐标。
    """
    # 配置支持中文的非衬线字体（默认的字体无法显示中文）
    plt.rcParams["font.sans-serif"] = ["SimHei", "Songti SC", "STFangsong"]
    # 使用指定的中文字体时需要下面的配置来避免负号无法显示
    plt.rcParams["axes.unicode_minus"] = False

    series_for_draw = pd.Series({"一季度": 400, "二季度": 520, "三季度": 180, "四季度": 380})
    logging.info(f"ser9:{series_for_draw}")

    # 通过Series对象的plot方法绘图（kind='bar'表示绘制柱状图）
    series_for_draw.plot(kind="bar", color=["r", "g", "b", "y"])
    # x轴的坐标旋转到0度（中文水平显示）
    plt.xticks(rotation=0)
    # 在柱状图的柱子上绘制数字
    for i in range(4):
        # 绘制数字的4个参数，分别是 x轴位置、y轴位置、数字的值、 模式
        plt.text(i, series_for_draw[i] + 5, series_for_draw[i], ha="center")
    # 显示图像
    plt.show()

    # （kind='pie'表示绘制饼状图）autopct参数可以配置在饼图上显示每块饼的占比
    series_for_draw.plot(kind="pie", autopct="%.1f%%")
    # 设置y轴的标签（显示在饼图左侧的文字）
    plt.ylabel("各季度占比")
    plt.show()
