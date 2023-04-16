# Scrapy

Scrapy相关demo 

## 免责声明
1. 若使用者滥用本项目,本人 无需承担 任何法律责任. 
2. 本程序仅供娱乐,源码全部开源,禁止滥用和二次贩卖盈利. 禁止用于商业用途.



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
    Scrapy中文： https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html

#### 启动

    cd crawler/my_scrapy/hello_world_demo/hello_world_demo/spiders/
    scrapy crawl douban -o result.json            #运行并保存


### get_cartoon

#### 项目介绍

get_cartoon是一个scrapy的漫画爬虫

#### 相关文档
    
    Scrapy： https://docs.scrapy.org/en/latest/intro/overview.html

#### 启动

    cd crawler/my_scrapy/get_cartoon/get_cartoon/spiders/
    scrapy crawl manhuagui -o result.json            #运行并保存

## 卸载项目

    pyenv virtualenv-delete my-scrapy
 

