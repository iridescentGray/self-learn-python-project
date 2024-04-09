from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get("http://www.baidu.com")

    # 隐式等待10s
    # 隐式等待：接指定一个等待时间，过了指定的等待时间，不管页面加载情况如何都开始获取元素
    driver.implicitly_wait(3)

    # 显示等待：等待某个条件成立
    revealed = driver.find_element(By.ID, "revealed")
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d: revealed.is_displayed())
