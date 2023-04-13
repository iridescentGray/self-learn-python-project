# Scrapy

Scrapy相关demo 

## 环境搭建

### 通过pyenv的virtualenv插件使用

    pyenv virtualenv  3.10.9 my-scrapy  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate my-scrapy
    python -m pip install --upgrade pip
    cd crawler/my_scrapy 
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## 项目

### hello_world_demo

#### 项目介绍

hello_world_demo是一个scrapy的简单入门项目

#### 相关文档

    Scrapy： https://docs.scrapy.org/en/latest/intro/overview.html

#### 启动

    cd crawler/my_scrapy/hello_world_demo/hello_world_demo/spiders/
    scrapy crawl douban -o result.json            #运行并保存

## 卸载项目

    pyenv virtualenv-delete my-scrapy
 

