from pypika import Query, Field, Table, functions as fn

girl = Table("girl")

# fn 是一个模块，里面包含了很多的类，每个类对应一个聚合函数
sql = (
    Query.from_(girl)
    .select("age", fn.Count(Field("id")))
    .where(Field("length") < 160)
    .groupby(Field("age"))
)
print(sql)
