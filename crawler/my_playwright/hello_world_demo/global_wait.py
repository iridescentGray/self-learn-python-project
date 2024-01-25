from playwright.sync_api import sync_playwright


"""
playwright-doc:
https://playwright.dev/python/docs/debug
"""

with sync_playwright() as playwright:
    # slow_mo option to slow down execution (by N milliseconds per operation)
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    page.goto("https://google.com")
    page.goto("https://baidu.com")
    page.goto("https://google.com")

    page.close()
