import pandas as pd
import bar_chart_race as bcr

# 获取数据
df = pd.read_csv("acrobatics/bar_chart_race/covid19_tutorial.csv", index_col=["date"])

bcr.bar_chart_race(df, "acrobatics/bar_chart_race/imgout/common-time-desc.gif")
bcr.bar_chart_race(
    df, "acrobatics/bar_chart_race/imgout/common-time-asc.gif", sort="asc"
)

bcr.bar_chart_race(df, "acrobatics/bar_chart_race/imgout/colourful.gif", cmap="plotly3")

bcr.bar_chart_race(df, "acrobatics/bar_chart_race/imgout/bar.gif", orientation="v")

bcr.bar_chart_race(df, "acrobatics/bar_chart_race/imgout/limit_entry.gif", n_bars=6)

bcr.bar_chart_race(
    df, "acrobatics/bar_chart_race/imgout/fixed_length.gif", fixed_max=True
)

bcr.bar_chart_race(
    df, "acrobatics/bar_chart_race/imgout/frame_rate.gif", steps_per_period=3
)


# figsize：设置画布大小，默认 (6, 3.5)
# dpi：图像分辨率，默认 144
# label_bars：显示柱状图的数值信息，默认为 True；指定为 False 则不显示；指定为字典，则自定义显示属性
# period_label：显示时间标签信息，默认为 True；指定为 False 则不显示；指定为字典，则自定义显示属性
# period_fmt：设置日期格式
# title：图表标题
# title_size：标题字体大小
# shared_fontdict：全局字体属性，例如 {'family': 'Helvetica', 'weight': 'bold', 'color': 'rebeccapurple'}
bcr.bar_chart_race(
    df,
    "acrobatics/bar_chart_race/imgout/picture_settings.gif",
    figsize=(5, 3),
    dpi=100,
    label_bars=False,
    title="COVID-19 Deaths by Country",
)


bcr.bar_chart_race(
    df,
    "acrobatics/bar_chart_race/imgout/transparent.gif",
    bar_kwargs={"alpha": 0.2, "ec": "black", "lw": 3},
)
