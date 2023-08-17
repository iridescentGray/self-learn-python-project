import peewee

db = peewee.MySQLDatabase(
    "test_peewee", host="localhost", port=3306, user="root", password="123456"
)
