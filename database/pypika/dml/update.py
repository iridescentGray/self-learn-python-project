from pypika import Table, Query

table = Table("t")
sql = Query.update(table).set(table.name, "u1")
print(sql)
sql = Query.update(table).set(table.name, "u2").where(table.id == 1)
print(sql)
sql = Query.update(table).set(table.name, "u3").set(table.age, 16)
print(sql)

table1 = Table("t1")
table2 = Table("t2")

sql = (
    Query.update(table1)
    .join(table2)
    .on(table1.uid == table2.tid)
    .set(table1.name, table2.name)
    .where(table1.uid > 10)
)
print(sql)
