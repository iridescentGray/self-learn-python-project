import os
from datetime import timedelta

# 数据库相关配置
# 建议在本地根目录下新建 .env 文件维护敏感信息配置项更安全
# 用户名
USERNAME = os.getenv("MYSQL_USER_NAME")
# 密码
PASSWORD = os.getenv("MYSQL_USER_PASSWORD")
# 地址
HOSTNAME = os.getenv("MYSQL_HOSTNAME")
# 端口
PORT = os.getenv("MYSQL_PORT")
# 数据库名称
DATABASE = os.getenv("MYSQL_DATABASE_NAME")

# 固定格式 不用改
DIALECT = "mysql"
DRIVER = "pymysql"


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
        DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE
    )
    SQLALCHEMY_ECHO = True
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_BLOCKLIST_TOKEN_CHECKS = ["access"]


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ""


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
