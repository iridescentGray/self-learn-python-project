# 数据分析入门

数据分析入门demo

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

### data_analysis_hello_world

#### introduce

data_analysis_hello_world是一个数据分析的入门项目,介绍基础Api的使用

#### start-up
    

### my_seaborn

#### introduce

my_seaborn是介绍seaborn用法的项目
Seaborn 是建立在 matplotlib 之上的数据可视化工具，它相当于是对 matplotlib 进行了更高级的封装，
而且 seaborn 也能跟 pandas 无缝整合，让我们可以用更少的代码构建出更好的统计图表，帮助我们探索和理解数据

#### start-up

#### Related documents

    seaborn：
        https://seaborn.pydata.org/tutorial.html
        https://github.com/mwaskom/seaborn


## uninstall

    pyenv deactivate data_analysis_hello_world
    pyenv virtualenv-delete data_analysis_hello_world