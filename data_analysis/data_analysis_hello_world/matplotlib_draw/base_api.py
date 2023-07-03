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
        f"----------------------------创建图片(基于plt)：同坐标系折线图------------------------------------------"
    )
    # figure()函数的返回值是一个Figure对象,它代表了绘图使用的画布
    # figsize- 指定画布的尺寸默认 [6.4, 4.8]
    # dpi-     设置绘图的分辨率
    # facecolor- 设置画布的背景色
    line_chart_in_the_same_coordinate_figure = plt.figure(figsize=(8, 4), dpi=120, facecolor='darkgray')
    logging.info(f"figure return a {type(line_chart_in_the_same_coordinate_figure)}")

    # 三个参数分别用来指定整个画布分成几行几列以及当前坐标系的索引,这三个参数的默认值都是1
    line_chart_in_the_same_coordinate = line_chart_in_the_same_coordinate_figure.add_subplot(2, 2,
                                                                                             1)  # 使用add_subplot给画布创建一个或多个子图
    # subplot方法返回一个坐标系对象 matplotlib.axes._axes.Axes
    logging.info(f"subplot return a {type(line_chart_in_the_same_coordinate)}")

    line_chart_in_the_same_coordinate.set_title("同坐标系折线图")
    x = np.linspace(-2 * np.pi, 2 * np.pi, 120)
    y1, y2 = np.sin(x), np.cos(x)
    # linewidth 定制折线的粗细 linestyle 定制折线的样式 marker参数来定制数据点的标记  color来定制折线的颜色
    line_chart_in_the_same_coordinate.plot(x, y1, linewidth=2, marker='*', color='red')
    line_chart_in_the_same_coordinate_plot = line_chart_in_the_same_coordinate.plot(x, y2, linewidth=2, marker='*',
                                                                                    color='blue')
    # plot方法返回一个list,list中的对象是matplotlib.lines.Line2D
    logging.info(f"plot return a {type(line_chart_in_the_same_coordinate_plot)}")
    for obj in line_chart_in_the_same_coordinate_plot:
        logging.info(f"plot return a {type(obj)}")
    # 显示绘图
    plt.show()

    logging.info(
        f"----------------------------在图中新建子图(基于面向对象): 分离坐标系折线图------------------------------------------"
    )
    # 使用plt 可以代替面向对象操作

    # ：使用subplot创建两个坐标系即可
    plt.figure(figsize=(8, 4), dpi=120)
    # 创建坐标系（第1个图）
    separate_coordinate1 = plt.subplot(2, 1, 1)
    separate_coordinate1.plot(x, y1, linewidth=2, marker='*', color='red')
    # 创建坐标系（第2个图）
    separate_coordinate2 = plt.subplot(2, 1, 2)
    separate_coordinate2.plot(x, y2, linewidth=2, marker='^', color='blue')
    plt.show()

    logging.info(
        f"----------------------------在图中添加新坐标系(基于面向对象)：嵌套坐标系折线图------------------------------------------"
    )
    fig = plt.figure(figsize=(10, 4), dpi=120)
    plt.plot(x, y1, linewidth=2, marker='*', color='red')

    # 参数代表了新坐标系在原坐标系中的位置
    ax = fig.add_axes((0.595, 0.6, 0.3, 0.25))  # add_axes方法在现有坐标系中嵌套一个新的坐标系
    # 前两个值是左下角的位置,后两个值是坐标系的宽度和高度
    ax.plot(x, y2, marker='^', color='blue')
    ax = fig.add_axes((0.155, 0.2, 0.3, 0.25))
    ax.plot(x, y2, marker='^', color='green')

    plt.show()

    logging.info(
        f"----------------------------保存图片(基于面向对象)：随机数折线图------------------------------------------"
    )
    will_save_plt_figure = plt.figure(figsize=(10, 4), dpi=120)
    will_save_plt_ax = will_save_plt_figure.add_subplot(1, 1, 1)
    will_save_plt_ax.plot(np.random.randn(1000).cumsum())
    # plt.savefig将活动图片保存到文件。这个方法等价于图片对象的savefig实例方法
    plt.savefig('chart.png', dpi=400, bbox_inches='tight')
    # saveifg并非一定是写到硬盘的，它可以将图片写入到所有的文件型对象中，例如BytesIO：
