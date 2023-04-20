# 数据分析入门

数据分析入门demo

## 环境搭建

### 通过pyenv的virtualenv插件使用

    pyenv virtualenv  3.10.9 data_analysis_hello_world  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate data_analysis_hello_world
    python -m pip install --upgrade pip
    cd data_analysis/data_analysis_hello_world
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## 项目

### data_analysis_hello_world

#### 项目介绍

data_analysis_hello_world是一个数据分析的入门项目

#### 相关文档

    jupyter：
        https://zhuanlan.zhihu.com/p/32320214
    numpy：
    pandas：
    matplotlib：

#### 启动

    启动jupyter: jupyter notebook

## 卸载项目

    pyenv deactivate data_analysis_hello_world 
    pyenv virtualenv-delete data_analysis_hello_world
 

