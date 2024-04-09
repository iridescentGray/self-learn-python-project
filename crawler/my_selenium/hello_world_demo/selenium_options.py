import time

from selenium import webdriver

# 使用开发者模式
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])

with webdriver.Chrome(options=options) as driver:
    driver.get("https://www.baidu.com")
    time.sleep(2)

# 更改为无头模式（不打开浏览器）
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("–-disable-dev-shm-usage")
options.add_argument("--headless")

with webdriver.Chrome(options=options) as driver:
    print("run as headless")
    driver.get("https://www.baidu.com")
    time.sleep(1)

# 以移动端模式打开
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", {"deviceName": "Nexus 7"})

with webdriver.Chrome(options=options) as driver:
    driver.get("https://www.baidu.com")
    time.sleep(1)
