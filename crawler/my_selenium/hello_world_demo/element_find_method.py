from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

# selenium 获取元素通过 python 原生实现，速度没使用 C 语言实现的 lxml 模块快

driver.find_element(By.ID, "id_name")  # 获取符合条件的第一个元素
driver.find_elements(By.ID, "id_name")  # 获取符合条件的多个元素
# 根据类名查找元素

driver.find_element(By.CLASS_NAME, "class_name")
driver.find_elements(By.CLASS_NAME, "class_name")
# 根据name属性的值来查找元素

driver.find_element(By.NAME, "username")
# 根据标签名来查找元素

driver.find_element(By.TAG_NAME, "div")
# 根据xpath语法来选择元素

driver.find_element(By.XPATH, "//div[@class='哈哈']/a")

# 根据css选择器选择元素
driver.find_element(By.CSS_SELECTOR, "banner")
