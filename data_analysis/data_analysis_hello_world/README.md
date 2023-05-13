# 数据分析入门

数据分析入门demo

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 data_analysis_hello_world  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate data_analysis_hello_world
    python -m pip install --upgrade pip
    cd data_analysis/data_analysis_hello_world
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## project

### data_analysis_hello_world

#### Project Introduction

data_analysis_hello_world是一个数据分析的入门项目

#### Related documents

    jupyter：
        - https://zhuanlan.zhihu.com/p/32320214
    numpy：
        - https://www.pythonprogramming.in/numpy-tutorial-with-examples-and-solutions.html
    pandas：
    matplotlib：

#### start-up

    start-up jupyter: jupyter notebook

## uninstall

    pyenv deactivate data_analysis_hello_world
    pyenv virtualenv-delete data_analysis_hello_world
