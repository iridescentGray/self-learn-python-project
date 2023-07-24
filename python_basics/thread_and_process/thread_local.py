import threading

local = threading.local()


def get():
    name = threading.current_thread().name
    # 获取绑定在 local 上的 value
    value = local.value
    print(f"线程: {name}, value: {value}")


def set_():
    name = threading.current_thread().name
    # 为不同的线程设置不同的值
    if name == "one":
        local.value = "ONE"
    elif name == "two":
        local.value = "TWO"
    # 执行 get 函数
    get()


t1 = threading.Thread(target=set_, name="one")
t2 = threading.Thread(target=set_, name="two")
t1.start()
t2.start()
