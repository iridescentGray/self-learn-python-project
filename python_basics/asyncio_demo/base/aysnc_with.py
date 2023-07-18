import asyncio

print(f"-----------------------------------------use async with------------------------------------------")


class Conn:

    async def __aenter__(self):
        print("创建连接")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("释放连接")


async def main():
    async with Conn() as conn:
        print(conn)
        print("code")


asyncio.run(main())
