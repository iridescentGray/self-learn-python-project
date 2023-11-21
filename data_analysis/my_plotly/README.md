# 入门
plotly有两个核心概念,分别是 轨迹 和 画布

## 轨迹 和 画布
图表被称为轨迹(trace).而 轨迹 必须显示在画布上
一个画布可以显示多个轨迹。
详细请从这里了解：
https://plotly.com/python/reference/index/

### 常见轨迹

#### 2D
* AngularAxis：极坐标图表
* Area：区域图
* Bar：柱状图
* Barpolar：极坐标柱状图
* Box：盒形图，又称箱型图
* Candlestick和Ohlc：金融股票行业常用的k线图和OHLC曲线图
* ColorBar：彩条图
* Contour：轮廓图
* Choropleth：等值线图
* Line：曲线图
* Heatmap：热点图
* Histogram：直方图
* Histogram2d：2d平面直方图
* Histogram2dContour：2d轮廓直方图
* Scatter：散点图、折线图

#### 3D

* Scatter3d：3d立体散点图、折线图
* Surface：表面图
* Mesh3d：3d立体网格图
* Pointcloud：云点图

#### 地图

* Scattergeo：基于地图模式的散点图、折线图
* Choropleth：立体等值线图
* Scattermapbox：基于地图的散点图

## API分组

* Scatter
1.  能够用来绘制area_chat、line_chat、scatter_plot，功能较多

