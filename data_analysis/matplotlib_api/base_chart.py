import logging

import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    """
        matplotlib绘制各种图:
        更多例子查看官方网站：
        https://matplotlib.org/stable/gallery/index.html
    """
    # 配置支持中文的非衬线字体（默认的字体无法显示中文）
    plt.rcParams["font.sans-serif"] = ["SimHei", "Songti SC", "STFangsong"]
    # 使用指定的中文字体时需要下面的配置来避免负号无法显示
    plt.rcParams['axes.unicode_minus'] = False

    logging.info(
        f"----------------------------散点图 scatter------------------------------------------"
    )
    plt.scatter(np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000]),
                np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500]))
    plt.title('散点图 scatter')
    plt.show()

    logging.info(
        f"----------------------------柱状图 bar------------------------------------------"
    )
    plt.figure(figsize=(6, 4), dpi=120)
    # 通过横坐标的偏移，让两组数据对应的柱子分开
    # width参数控制柱子的粗细，label参数为柱子添加标签
    plt.bar(np.random.randint(20, 30, 4), np.random.randint(40, 50, 4), width=0.2, label='Sales Group A')
    plt.bar(np.random.randint(20, 30, 4) + 0.1, np.random.randint(40, 50, 4), width=0.2, label='Sales Group B')
    # 定制显示图例 Sales Group A/B
    plt.title('柱状图 bare')
    plt.legend()
    plt.show()

    logging.info(
        f"----------------------------饼状图 pie------------------------------------------"
    )
    plt.figure(figsize=(5, 5), dpi=120)
    plt.pie(
        x=np.random.randint(100, 500, 7),
        # 标签
        labels=['苹果', '香蕉', '桃子', '荔枝', '石榴', '山竹', '榴莲'],
        # 自动显示百分比
        autopct='%.1f%%',
        # 饼图的半径
        radius=1,
        # 百分比到圆心的距离
        pctdistance=0.8,
        # 颜色（随机生成）
        colors=np.random.rand(7, 3),
        # 分离距离
        # explode=[0.05, 0, 0.1, 0, 0, 0, 0],
        # 阴影效果
        # shadow=True,
        # 字体属性
        textprops=dict(fontsize=8, color='black'),
        # 楔子属性（生成环状饼图的关键）
        wedgeprops=dict(linewidth=1, width=0.35)
    )
    # 定制图表的标题
    plt.title('饼状图 pie')
    plt.show()

    logging.info(
        f"---------------------------直方图 hist------------------------------------------"
    )
    bins = np.array([150, 155, 160, 165, 170, 175, 180, 185, 190])

    plt.figure(figsize=(6, 4), dpi=120)
    # density参数默认值为False，表示纵轴显示频数
    # 将density参数设置为True，纵轴会显示概率密度
    plt.hist(np.random.randint(140, 180, 50), np.arange(150, 180, 5), density=True)
    # 定制横轴标签
    plt.xlabel('身高')
    # 定制纵轴标签
    plt.ylabel('概率密度')
    plt.title('直方图 hist')
    plt.show()
