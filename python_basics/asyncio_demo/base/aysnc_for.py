import asyncio


class A:
    def __init__(self):
        self.l = [1, 2, 3, 4]
        self.__index = 0

    # 注意：定义 __aiter__ 是不需要 async 的
    def __aiter__(self):
        return self

    # 但是定义 __anext__ 需要 async
    async def __anext__(self):
        try:
            res = self.l[self.__index]
            self.__index += 1
            return res
        except IndexError:
            # 捕获异常，协程则要raise一个StopAsyncIteration
            raise StopAsyncIteration


async def main():
    async for _ in A():
        print(_)


asyncio.run(main())
