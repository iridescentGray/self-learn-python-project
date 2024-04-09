import time

from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get("https://www.baidu.com")

    # 在js中，通过window.open打开新窗口
    driver.execute_script("window.open('https://www.bilibili.com')")
    time.sleep(2)
    print(f"driver.current_url is: {driver.current_url}")  # https://www.bilibili.com/

    # 以前是driver.switch_to_window，这方法此时还能用，但是已经提示我们要被移除了
    # 建议我们使用driver.switch_to.window
    driver.switch_to.window(driver.window_handles[1])  # 切换到bilibili

    # 打印当前页面的url
    print(f"driver.current_url is: {driver.current_url}")  # https://www.bilibili.com/
    driver.close()
    time.sleep(2)
