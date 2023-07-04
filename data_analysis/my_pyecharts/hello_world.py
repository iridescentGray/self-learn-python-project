import logging

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Map
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    simple_bar = Bar()
    simple_bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    simple_bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    # 也可以传入路径参数，如 bar.render("mycharts.html")
    simple_bar.render("simple_bar.html")

    # 链式调用
    chain_bar = (
        Bar().add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    )
    chain_bar.render("chain_bar.html")

    # 设置主题
    theme_bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
            .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
            .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    )
    theme_bar.render("theme_bar.html")

    interactive_bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='600px', height='450px'))
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
            .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
            .add_yaxis("商家C", [12, 32, 40, 52, 35, 26])
            .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
                             toolbox_opts=opts.ToolboxOpts(orient='vertical', pos_left='right'))
    )
    interactive_bar.render("interactive_bar.html")

    geography_data = [
        ('贵州省', 39), ('新疆维吾尔自治区', 3), ('内蒙古自治区', 3), ('西藏自治区', 35)
    ]
    map_chart = Map()
    map_chart.add('', geography_data, 'china', is_roam=False)
    map_chart.render("geography_data.html")
