import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://www.baidu.com")
    baidu_input_tag = driver.find_element(By.ID, "kw")
    baidu_input_tag.send_keys("test send_keys")  # 向input框输入内容
    time.sleep(1)

    baidu_input_tag.clear()  # 清除input框的内容
    time.sleep(1)

    baidu_input_tag.send_keys("test search")  # 向input框输入内容

    baidu_search_tag = driver.find_element(By.ID, "su")  # 点击搜索按钮
    baidu_search_tag.click()
    time.sleep(2)
