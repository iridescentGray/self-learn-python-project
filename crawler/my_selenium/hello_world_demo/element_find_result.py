from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("http://www.baidu.com")

tag = driver.find_element(By.ID, "kw")
# 得到的tag依旧可以使用find_element_by_xxx等方法
# 但除此之外还有哪些属性呢

print(type(tag))

# 拿到当前的标签名，既然我们获取的是输入框，应该是input
print(tag.tag_name)  # input

# 拿到标签对应的文本，有可能为空，所以我们用%r打印
print(f"tag.text: {tag.text}")  # ''

# 获取位置
print(tag.location)  # {'x': 152, 'y': 310}

# 获取尺寸
print(tag.size)  # {'height': 22, 'width': 500}

# 获取元素attr
print(tag.get_attribute("type"))  # text
print(tag.get_attribute("autocomplete"))  # off
print(tag.get_attribute("class"))  # s_ipt
