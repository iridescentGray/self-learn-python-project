import peewee
from connection import db


class Girl(peewee.Model):
    pk = peewee.AutoField(verbose_name="id")
    name = peewee.CharField(max_length=200, verbose_name="姓名")
    where = peewee.CharField(max_length=200, verbose_name="住址", help_text="测试")

    class Meta:
        # 绑定上面的数据库实例
        database = db
        # 设置表名
        table_name = "girl"


if __name__ == "__main__":
    # Use Model To Create Table
    db.create_tables([Girl])
    print(db.is_closed())  # False

    # 也可以手动关闭连接
    db.close()
    print(db.is_closed())  # True
