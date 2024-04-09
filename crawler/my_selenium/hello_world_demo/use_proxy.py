import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://127.0.0.1:7890")


with webdriver.Chrome(options=options) as driver:
    driver.get("https://www.google.com")
    time.sleep(3)
