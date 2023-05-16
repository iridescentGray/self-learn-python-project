# Scrapy

Scrapy相关demo

## 免责声明
1. 若使用者滥用本项目,本人 无需承担 任何法律责任.
2. 本程序仅供娱乐,源码全部开源,禁止滥用和二次贩卖盈利. 禁止用于商业用途.



## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 my-scrapy  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate my-scrapy
    python -m pip install --upgrade pip
    cd crawler/my_scrapy
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/


### Related documents

    Scrapy：    https://docs.scrapy.org/en/latest/intro/overview.html
    Scrapy中文： https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html
    scrapy-playwright： https://github.com/scrapy-plugins/scrapy-playwright
    playwright-python-doc:   https://playwright.dev/python/docs/intro
    playwright-python-api:   https://playwright.dev/python/docs/api/class-playwright

## uninstall

    pyenv virtualenv-delete my-scrapy

## project

### hello_world_demo

#### introduce

hello_world_demo是一个scrapy的简单入门项目

#### start-up

    cd crawler/my_scrapy/hello_world_demo/hello_world_demo/spiders/
    scrapy crawl douban -o result.json            #运行并保存


### get_cartoon

#### introduce

get_cartoon是一个scrapy的漫画爬虫

#### start-up
    playwright install chromium
    cd /crawler/my_scrapy/get_cartoon/get_cartoon/spiders/
    scrapy crawl manhuagui


### scrapy_playwright_demo

#### introduce

scrapy_playwright_demo include Official document demo and own demo

#### start-up
    playwright install chromium
    cd crawler/my_scrapy/scrapy_playwright_demo/scrapy_playwright_demo/spiders/
    scrapy crawl scroll_and_shot_all_screen  

