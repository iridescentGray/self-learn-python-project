from multiprocessing import Pool


def say_hello(name) -> str:
    return f"hello, {name}"


def hello_world_pool():
    with Pool() as pool:
        # apply() method will block until the function execution completed
        hi1 = pool.apply(say_hello, args=("jenn",))
        hi2 = pool.apply(say_hello, args=("ben",))
        print(hi1)
        print(hi2)


def async_apply_pool():
    with Pool() as pool:
        hi1 = pool.apply_async(say_hello, args=("satori",))
        hi2 = pool.apply_async(say_hello, args=("koishi",))
        print(type(hi1))  # <class 'multiprocessing.pool.ApplyResult'>
        # get() method will block until completed
        print(hi1.get())
        print(hi2.get())


if __name__ == "__main__":
    hello_world_pool()
    async_apply_pool()
