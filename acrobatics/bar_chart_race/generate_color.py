from pprint import pprint

import bar_chart_race as bcr
import pandas as pd
from bar_chart_race._colormaps import colormaps

df = pd.read_csv("acrobatics/bar_chart_race/covid19_tutorial.csv", index_col=["date"])

print("----------------------------All Color------------------------------")
pprint(list(colormaps.keys()))


print(
    "----------------------------use color Draw a picture------------------------------"
)
bcr.bar_chart_race(df, "acrobatics/bar_chart_race/imgout/colourful.gif", cmap="plotly3")


print("----------------------------not repetition color------------------------------")
bcr.bar_chart_race(
    df,
    "acrobatics/bar_chart_race/imgout/no_repetition.gif",
    cmap="plotly3",
    filter_column_colors=True,
)
