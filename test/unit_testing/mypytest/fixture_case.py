import random
import string

import pytest

"""
在编写单元测试时,我们常常需要重复用到一些东西。
在pytest框架下,你可以非常方便地用@pytest.fixture装饰器创建fixture重复使用对象。
fixture是pytest最为核心的功能之一。通过定义fixture,你可以快速创建出一些可复用的测试固定件,并在每个测试的开始和结束阶段自动执行特定的代码逻辑。

"""

"""
在为某模块编写测试代码时,我需要不断用到一个长度为32的随机token字符串。
为了简化测试代码,我可以创造一个名为random_token的fixture

fixture还有一个非常重要的概念:作用域(scope},共五种作用域,它们的区别如下:
(1} function(函数}:默认作用域,结果会在每个测试函数结束后销毁。
(2} class(类}:结果会在执行完类里的所有测试方法后销毁。
(3} module(模块}:结果会在执行完整个模块的所有测试后销毁。
(4} package(包}:结果会在执行完整个包的所有测试后销毁。
(5}session(测试会话}:结果会在测试会话(也就是一次完整的pytest执行过程}结束后销毁。
"""


@pytest.fixture(scope="session")
def random_token() -> str:
    """生成随机 token"""
    token_l = []
    char_pool = string.ascii_lowercase + string.digits
    for _ in range(32):
        token_l.append(random.choice(char_pool))
    return "".join(token_l)


def create_db_conn():
    return open("fixture_case.py", "r")


# fixture函数中使用yield关键字,把它变成一个生成器函数,那么就能为fixture增加额外的清理逻辑。
@pytest.fixture
def db_connection():
    """创建并返回一个数据库连接"""
    conn = create_db_conn()
    yield conn
    conn.close()


# autouse指定为True可以创建一个会自动执行的fixture,在每个测试方法的开始与结束阶段自动执行
@pytest.fixture(autouse=True)
def prepare_data():
    print("load resource")
    yield
    # 在测试结束时,创建两个用户
    print("clear resource")


def test_token(random_token):
    print(random_token)


def test_db_connection(db_connection):
    print(db_connection)
