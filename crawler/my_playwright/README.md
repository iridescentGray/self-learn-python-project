# Playwright

Playwright相关demo


## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 my_playwright  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate my_playwright
    python -m pip install --upgrade pip
    cd crawler/my_playwright
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## introduce

### hello_world_demo

#### Project Introduction

hello_world_demo是一个scrapy的简单入门项目

#### Related documents

    Scrapy： https://docs.scrapy.org/en/latest/intro/overview.html
    Scrapy中文： https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html

#### start-up

    cd crawler/my_scrapy/hello_world_demo/hello_world_demo/spiders/
    scrapy crawl douban -o result.json            #运行并保存


## uninstall

    pyenv virtualenv-delete my_playwright
