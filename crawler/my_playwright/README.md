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

## uninstall

    pyenv virtualenv-delete my_playwright
