# Playwright

Playwright相关demo


## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 my_playwright  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate my_playwright
    python -m pip install --upgrade pip
    cd crawler/my_playwright
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
    playwright install chromium

### Related documents

    playwright-python-doc:   https://playwright.dev/python/docs/intro
    playwright-python-api:   https://playwright.dev/python/docs/api/class-playwright

## introduce

### hello_world_demo

#### introduce

hello_world_demo是一个playwright的简单入门项目

#### start-up


## uninstall

    pyenv virtualenv-delete my_playwright
