from pypika import Query


sql = Query.from_("t").select("id", "name", "age")
# 是一个 QueryBuilder 对象
print(sql.__class__)
print(sql)  # SELECT "id","name","age" FROM "t"
print(str(sql))  # SELECT "id","name","age" FROM "t"
print(sql.get_sql())  # SELECT "id","name","age" FROM "t"
