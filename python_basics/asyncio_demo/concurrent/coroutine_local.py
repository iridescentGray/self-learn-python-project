import asyncio
import contextvars

coroutine_local = contextvars.ContextVar("debug tag")


async def get_from_coroutine1():
    print(coroutine_local.get())
    # nesting will not effect correct result
    await get_from_coroutine2()


async def get_from_coroutine2():
    print(coroutine_local.get())


async def set_to_coroutine(val):
    coroutine_local.set(val)
    await get_from_coroutine1()
    await get_from_coroutine2()


async def main():
    coro1 = set_to_coroutine("coroutine_1")
    coro2 = set_to_coroutine("coroutine_2")
    await asyncio.gather(coro1, coro2)


asyncio.run(main())
