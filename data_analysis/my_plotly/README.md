# 入门

plotly 有两个核心概念,分别是 轨迹 和 画布

## Related documents

    plotly: https://github.com/plotly/plotly.py
    plotly-doc：https://plotly.com/python/

## 轨迹 和 画布

图表被称为轨迹(trace).而 轨迹 必须显示在画布上
一个画布可以显示多个轨迹。
详细请从这里了解：
https://plotly.com/python/reference/index/

### 常见轨迹

#### 2D

- AngularAxis：极坐标图表
- Area：区域图
- Bar：柱状图
- Barpolar：极坐标柱状图
- Box：盒形图，又称箱型图
- Candlestick 和 Ohlc：金融股票行业常用的 k 线图和 OHLC 曲线图
- ColorBar：彩条图
- Contour：轮廓图
- Choropleth：等值线图
- Line：曲线图
- Heatmap：热点图
- Histogram：直方图
- Histogram2d：2d 平面直方图
- Histogram2dContour：2d 轮廓直方图
- Scatter：散点图、折线图

#### 3D

- Scatter3d：3d 立体散点图、折线图
- Surface：表面图
- Mesh3d：3d 立体网格图
- Pointcloud：云点图

#### 地图

- Scattergeo：基于地图模式的散点图、折线图
- Choropleth：立体等值线图
- Scattermapbox：基于地图的散点图

## API 分组

- Scatter

1.  能够用来绘制 area_chat、line_chat、scatter_plot，功能较多
