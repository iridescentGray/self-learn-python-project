import time


def get_do():
    time.sleep(1)
    print("get_do")
    return True


while response := get_do():
    print(response)
    print("do")
