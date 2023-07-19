import asyncio

from sqlalchemy import text

from engine import mysql_engine as engine


async def get_data():
    async with engine.connect() as conn:
        query = text("SELECT * FROM girls")
        result = await conn.execute(query)

    columns = result.keys()
    print(f"result.keys(): {columns}")
    data = result.fetchone()
    print(f"result.fetchone(): {data}")
    print(f"dict(zip(columns, data): {dict(zip(columns, data))}")

    print(result.fetchone())
    print(result.fetchone())
    print(result.fetchone())
    print(result.fetchone())  # 没有数据时，就会返回 None


asyncio.run(get_data())
