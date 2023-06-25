import logging

import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    """
        matplotlib是专业的绘图库
    """

    # 配置支持中文的非衬线字体（默认的字体无法显示中文）
    plt.rcParams["font.sans-serif"] = ["SimHei", "Songti SC", "STFangsong"]
    # 使用指定的中文字体时需要下面的配置来避免负号无法显示
    plt.rcParams['axes.unicode_minus'] = False

    logging.info(
        f"----------------------------同坐标系折线图------------------------------------------"
    )
    # figure()函数的返回值是一个Figure对象，它代表了绘图使用的画布
    # figsize- 指定画布的尺寸默认 [6.4, 4.8]
    # dpi-     设置绘图的分辨率
    # facecolor- 设置画布的背景色
    plt.figure(figsize=(8, 4), dpi=120, facecolor='darkgray')
    # subplot函数用于创建坐标系，该函数会返回Axes对象，也可以通过上面创建的Figure对象的add_subplot方法或add_axes方法来创建坐标系
    # 前三个参数分别用来指定整个画布分成几行几列以及当前坐标系的索引，这三个参数的默认值都是1
    plt.subplot(2, 2, 1)
    x = np.linspace(-2 * np.pi, 2 * np.pi, 120)
    y1, y2 = np.sin(x), np.cos(x)
    # linewidth 定制折线的粗细 linestyle 定制折线的样式 marker参数来定制数据点的标记  color来定制折线的颜色
    plt.plot(x, y1, linewidth=2, marker='*', color='red')
    plt.plot(x, y2, linewidth=2, marker='*', color='blue')
    # 显示绘图
    plt.show()

    logging.info(
        f"----------------------------分离坐标系折线图------------------------------------------"
    )
    # ：使用subplot创建两个坐标系即可
    plt.figure(figsize=(8, 4), dpi=120)
    # 创建坐标系（第1个图）
    plt.subplot(2, 1, 1)
    plt.plot(x, y1, linewidth=2, marker='*', color='red')
    # 创建坐标系（第2个图）
    plt.subplot(2, 1, 2)
    plt.plot(x, y2, linewidth=2, marker='^', color='blue')
    plt.show()

    logging.info(
        f"----------------------------嵌套坐标系折线图------------------------------------------"
    )
    fig = plt.figure(figsize=(10, 4), dpi=120)
    plt.plot(x, y1, linewidth=2, marker='*', color='red')

    # 用Figure对象的add_axes方法在现有坐标系中嵌套一个新的坐标系
    # 参数代表了新坐标系在原坐标系中的位置
    ax = fig.add_axes((0.595, 0.6, 0.3, 0.25))
    # 前两个值是左下角的位置，后两个值是坐标系的宽度和高度
    ax.plot(x, y2, marker='^', color='blue')
    ax = fig.add_axes((0.155, 0.2, 0.3, 0.25))
    ax.plot(x, y2, marker='^', color='green')
    plt.show()

    logging.info(
        f"----------------------------散点图------------------------------------------"
    )
    x = np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000])
    y = np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500])

    plt.figure(figsize=(6, 4), dpi=120)
    plt.scatter(x, y)
    plt.show()