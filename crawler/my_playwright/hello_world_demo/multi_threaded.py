"""

multi-threaded support

* Playwright's API is not thread-safe.
* you should create a playwright instance per thread  in a multi-threaded environment

playwright-doc:
https://playwright.dev/python/docs/library

"""
from threading import Thread

from playwright.sync_api import sync_playwright


def run1():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        page.wait_for_timeout(3000)
        page.close()


def run2():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        page.wait_for_timeout(1000)
        page.close()


def main():
    t = Thread(target=run1)
    t1 = Thread(target=run2)
    t.start()
    t1.start()
    t.join()
    t1.join()


main()
