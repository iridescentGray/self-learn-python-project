import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="IT空間 示範 streamlit",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={"About": "test"},
)


st.title("我的第一个应用程式")
st.subheader("两种最简单的写法")

st.write("尝试创建**表格**")
df = pd.DataFrame({"第1个栏位": ["a", "b", "c"], "第2个栏位": [10, 20, 30]})
df


st.subheader("绘制图表和地图")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
st.bar_chart(chart_data, color=["#8ECDDD", "#4F709C", "#E5D283"])
