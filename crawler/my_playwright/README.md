# Playwright

Playwright相关demo

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 my_playwright
    pyenv activate my_playwright
    python -m pip install --upgrade pip
    cd crawler/my_playwright
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
    playwright install chromium

### Related documents

    playwright-python-doc:   https://playwright.dev/python/docs/intro
    playwright-python-api:   https://playwright.dev/python/docs/api/class-playwright
    playwright-github:   https://github.com/microsoft/playwright


## ohter topic


### install browsers and dependencies
    browsers: https://playwright.dev/python/docs/browsers#google-chrome--microsoft-edge
    dependencies: https://playwright.dev/python/docs/browsers#install-system-dependencies

    get some help: playwright install --help

## uninstall

    pyenv virtualenv-delete my_playwright
