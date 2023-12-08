# 数据分析入门

数据分析入门 demo

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 data_analysis_hello_world  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate data_analysis_hello_world
    python -m pip install --upgrade pip
    cd data_analysis/data_analysis_hello_world
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    jupyter：
        - https://zhuanlan.zhihu.com/p/32320214
    numpy：
        - https://numpy.org/doc/stable/
        - https://www.pythonprogramming.in/numpy-tutorial-with-examples-and-solutions.html
    pandas：
        - https://pandas.pydata.org/docs/
    matplotlib：
        - https://matplotlib.org/

## project

### my_seaborn

#### introduce

my_seaborn 是介绍 seaborn 用法的项目
Seaborn 是建立在 matplotlib 之上的数据可视化工具，它相当于是对 matplotlib 进行了更高级的封装，
而且 seaborn 也能跟 pandas 无缝整合，让我们可以用更少的代码构建出更好的统计图表，帮助我们探索和理解数据

#### start-up

#### Related documents

    seaborn：
        https://seaborn.pydata.org/tutorial.html
        https://github.com/mwaskom/seaborn

### my_pyecharts

#### introduce

my_pyecharts 是介绍 pyecharts 用法的项目

1. Echarts 原来是百度开发的一个前端图表库，pyecharts 就是基于 Python 语言对 ECharts 进行了包装，
   让 Python 开发者也可以使用 ECharts 绘制外观精美且交互性强的统计图表。
2. pyecharts 并不能直接使用 NumPy 的 ndarray 和 Pandas 的 Series、DataFrame 为其提供数据，它需要的是 Python 原生的数据类型，所以如果有需要的时候就需要转化

#### start-up

#### Related documents

    pyecharts:
        https://pyecharts.org/
        https://github.com/pyecharts/pyecharts
    echarts:
        https://github.com/apache/echarts

## uninstall

    pyenv deactivate data_analysis_hello_world
    pyenv virtualenv-delete data_analysis_hello_world

### my_plotly

#### introduce

The interactive graphing library for Python

#### start-up

#### Related documents

     plotly: https://github.com/plotly/plotly.py
     plotly-doc：https://plotly.com/python/

### exercises

#### introduce

some exercises

#### start-up

#### Related documents

     source-github: https://github.com/rougier/numpy-100

## uninstall

    pyenv deactivate data_analysis_hello_world
    pyenv virtualenv-delete data_analysis_hello_world
