from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine

# 也可以直接传递一个字符串，参数和 create_engine 是一样的
# create_async_engine("mysql+asyncmy://...")
mysql_engine = create_async_engine(
    URL.create(
        "mysql+asyncmy",
        username="root",
        password="123456",
        host="localhost",
        port=3306,
        database="test_sqlalchemy",
    )
)
