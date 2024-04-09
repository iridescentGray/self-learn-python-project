from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get("http://www.baidu.com")

    # 获取所有cookie
    for cookie in driver.get_cookies():
        print(cookie)
        print("*" * 60)

    # 获取指定cookie
    print(f"get specify key: {driver.get_cookie('H_PS_PSSID')}")

    # 删除指定cookie
    driver.delete_cookie("H_PS_PSSID")
    # 删除之后，再获取一次
    print(f"get specify key: {driver.get_cookie('H_PS_PSSID')}")
