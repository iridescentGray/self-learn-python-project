import bar_chart_race as bcr
import matplotlib.pyplot as plt
import pandas as pd

# 设置字体，否则无法显示中文
plt.rcParams["font.sans-serif"] = ["SimHei"]  # Windows
# plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB'] # Mac
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("acrobatics/bar_chart_race/covid19_tutorial.csv", index_col=["date"])


def summary(values, ranks):
    # 动态文本的内容
    """
    values 为 df 的每一行（Series），例如
        Belgium            1143.0
        China              3326.0
        France             6520.0
        Germany            1275.0
        Iran               3294.0
        Italy             14681.0
        Netherlands        1490.0
        Spain             11198.0
        USA                7418.0
        United Kingdom     3611.0
        Name: 2020-04-03, dtype: float64

    ranks 则是针对 values 的值进行了排名，例如
        Belgium            1.0
        China              5.0
        France             7.0
        Germany            2.0
        Iran               4.0
        Italy             10.0
        Netherlands        3.0
        Spain              9.0
        USA                8.0
        United Kingdom     6.0
        Name: 2020-04-03, dtype: float64
    """
    all_people = int(values.sum())
    ranks_country = ranks.sort_values().index
    s = f"totol death: {all_people},  most death: {ranks_country[-1]},   least death:{ranks_country[0]}"
    # 设置文本位置、数值、大小、颜色等
    return {"x": 0.99, "y": 0.05, "s": s, "ha": "right", "size": 8}


# 添加文本
bcr.bar_chart_race(
    df, "acrobatics/bar_chart_race/imgout/dynamic.gif", period_summary_func=summary
)


# 设置垂直条数值，分位数
def vertical_bar(values, ranks):
    return values.quantile(0.9)


# 添加垂直条
bcr.bar_chart_race(
    df,
    "acrobatics/bar_chart_race/imgout/vertical_bar.gif",
    perpendicular_bar_func=vertical_bar,
)
