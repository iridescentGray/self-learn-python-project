import time

from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get("https://www.baidu.com")

    # 在js中，通过window.open打开新窗口
    driver.execute_script("window.open('https://www.bilibili.com')")
    time.sleep(2)
