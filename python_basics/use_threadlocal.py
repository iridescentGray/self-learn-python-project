import threading


# 创建一个 local 对象
thread_local = threading.local()


def get():
    name = threading.current_thread().name
    # 获取绑定在 local 上的 value
    value = thread_local.value
    print(f"线程 {name}, value: {value}")


def set_():
    name = threading.current_thread().name
    # 为不同的线程设置不同的值
    if name == "one":
        thread_local.value = "ONE"
    elif name == "two":
        thread_local.value = "TWO"
    # 执行 get 函数
    get()


t1 = threading.Thread(target=set_, name="one")
t2 = threading.Thread(target=set_, name="two")
t1.start()
t2.start()