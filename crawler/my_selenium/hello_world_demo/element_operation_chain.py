import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as driver:
    driver.get("https://www.baidu.com")

    # 获取input输入框
    input_btn = driver.find_element(By.ID, "kw")
    # 获取百度一下按钮
    baidu_btn = driver.find_element(By.ID, "su")

    # 这个类接收一个driver
    action_chains = ActionChains(driver)

    # 向指定的输入框里面输入内容
    action_chains.send_keys_to_element(input_btn, "test search")
    # 点击按钮
    action_chains.click(baidu_btn)
    # 以上相当于数据库里面的事务，然后调用perform执行链子上的操作
    action_chains.perform()
    time.sleep(2)
