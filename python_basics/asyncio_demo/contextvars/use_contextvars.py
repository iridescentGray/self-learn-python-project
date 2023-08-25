import asyncio
import contextvars

"""
一个协程内部 await 另一个协程,在另一个协程内部在 await另一个协程
不管套娃(await)多少次,它们获取contextvars的值都是一样的。

在任意一个协程内部都可以设置contextvars的值,后面的携程会获取到最后一次设置的值

"""

# ContextVar 支持默认值(get前没有先 set会抛出一个 LookupError),也可以在 get 中指定
context_var = contextvars.ContextVar("数据在协程之间隔离", default="哼哼")


async def get():
    # 获取值
    return context_var.get() + "~~~"


async def set_(val):
    # 设置值
    context_var.set(val)
    print(await get())


async def main():
    coro1 = set_("协程1")
    coro2 = set_("协程2")
    await asyncio.gather(coro1, coro2)


asyncio.run(main())
