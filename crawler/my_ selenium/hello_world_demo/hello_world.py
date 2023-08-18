from selenium import webdriver 

driver = webdriver.Chrome()

driver.get("http://www.baidu.com/s?wd=komeijisatori")

print(driver.page_source[0: 100])