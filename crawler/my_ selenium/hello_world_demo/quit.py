from selenium import webdriver 
import time 

driver = webdriver.Chrome()

driver.get("http://www.baidu.com/s?wd=komeijisatori")

time.sleep(5)  # 为了观察到现象，这里sleep 5秒

# close只会关闭最开始打开的页面
# driver.close()

#quit 的话，那么不仅页面、整个浏览器都会退出
# driver.quit()