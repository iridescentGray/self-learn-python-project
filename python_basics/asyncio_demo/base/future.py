import asyncio

# asyncio 里面有一个类 Future 和 Task，Task 是 Future 的子类，所以我们用的基本都是 task 对象，而不是 future 对象
# 但 Future 和 asyncio 的实现有着密不可分的关系
# 一个任务可以被认为是一个协程和一个 future的组合
print(
    f"-----------------------------------------Native Creation Future-------------------------------------------------"
)
native_future = asyncio.Future()

print(native_future)  # <Future pending>
print(native_future.__class__)  # <class '_asyncio.Future'>
print(f"future 是否完成: {native_future.done()}")  # future 是否完成: False

native_future.set_result("future_result")
print(f"future 是否完成: {native_future.done()}")
print(native_future)
print(f"future 的返回值: {native_future.result()}")

print(
    f"-----------------------------------------Use Future In Asyncio-------------------------------------------------"
)


async def set_future_value(future):
    await asyncio.sleep(1)
    future.set_result("Hello World future")


def make_request():
    future = asyncio.Future()
    # 创建一个任务来异步设置 future 的值
    asyncio.create_task(set_future_value(future))
    return future


async def use_future_in_asyncio():
    #  make_request是一个普通的函数，需要在协程里面调用
    future = make_request()
    print(f"future 是否完成: {future.done()}")
    # 阻塞等待，直到 future 有值，什么时候有值呢？
    # 显然是当协程 set_future_value 里面执行完 future.set_result 的时候
    value = await future  # 暂停 main()，直到 future 的值被设置完成
    print(f"future 是否完成: {future.done()}")
    print(value)


asyncio.run(use_future_in_asyncio())
print(
    f"-----------------------------------------Future Callback-------------------------------------------------"
)


def callback(future):
    print(f"future 已完成，值为 {future.result()}")


async def future_callback():
    test_future_callback = asyncio.Future()
    # 绑定一个回调，当 future 有值时会自动触发回调的执行
    test_future_callback.add_done_callback(callback)
    test_future_callback.set_result("res")


asyncio.run(future_callback())
