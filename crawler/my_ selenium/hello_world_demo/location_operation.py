import time
from selenium.webdriver.common.by import By
from selenium import webdriver 
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 获取标签
tag1 = driver.find_element(By.ID,"kw")

tag1.send_keys("test")

time.sleep(3)