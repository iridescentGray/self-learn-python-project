from pypika import Query, Table

table1 = Table("t1")
table2 = Table("t2")

sql = Query.from_(table1).select(table2.age, table1.name).left_join(table2).using("id")
print(sql)

sql = (
    Query.from_(table1)
    .select(table2.age, table1.name)
    .left_join(table2)
    .on(table1.field("uid") == table2.field("tid"))
)
print(sql)
