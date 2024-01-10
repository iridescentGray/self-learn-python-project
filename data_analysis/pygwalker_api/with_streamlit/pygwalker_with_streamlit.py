from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd
import streamlit as st

# 调整Streamlit页面的宽度
st.set_page_config(page_title="在Streamlit中使用PyGWalker", layout="wide")

# 在pygwalker和streamlit之间建立通信
init_streamlit_comm()

# 添加标题
st.title("在Streamlit中使用PyGWalker")


# 获取一个pygwalker渲染器的实例。你应该缓存这个实例，以有效地防止进程内存的增长。
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv(
        "https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv"
    )
    # 当你需要将你的应用程序发布给公众时，你应该将debug参数设置为False，以防止其他用户向你的图表配置文件中写入数据。
    return StreamlitRenderer(df, spec="./gw_config.json", debug=False)


renderer = get_pyg_renderer()

# 渲染你的数据探索界面。开发者可以使用它来通过拖放构建图表。
renderer.render_explore()
