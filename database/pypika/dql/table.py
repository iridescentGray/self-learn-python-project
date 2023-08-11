from pypika import Query, Table, Schema

print(
    f"------------------------------------------must declare table-----------------------------------------"
)

try:
    # must declare table
    sql = Query.select("id", "name", "age")
except Exception as e:
    print(e)  # Cannot select id, no FROM table specified.


print(
    f"-------------------------------------------Use Table Obj Build SQL-----------------------------------------"
)

table = Table("t")
sql = Query.from_(table).select(table.id, table.name, table.age)

print(str(sql))  # SELECT "id","name","age" FROM "t"

print(
    f"-------------------------------------------Table Alias-----------------------------------------"
)

table = Table("user").as_("t1")
sql = Query.from_(table).select(table.id, table.name, table.age)
print(str(sql))  # SELECT "t1"."id","t1"."name","t1"."age" FROM "t" "t1"

print(
    f"-------------------------------------------PostgreSQL Schema-----------------------------------------"
)
sch = Schema("my_schema")
# 对 Schema 对象直接通过属性引用的方式即可指定表名，比如 sch.t 就表示从 my_schema 下寻找名称为 t 的表
sql = Query.from_(sch.t).select(sch.t.id, sch.t.name, sch.t.age)
print(str(sql))  # SELECT "id","name","age" FROM "my_schema"."t"
