import time

# see https://docs.python.org/zh-cn/3/reference/expressions.html#assignment-expressions

def get_do():
    time.sleep(1)
    print("get_do")
    return True


while response := get_do():
    print(response)
    print("do")
