from pypika import Field, Query, Table

table = Table("t")
sql = Query.into(table).insert(1, "u1", 16, "p1")
print(sql)

sql = Query.into(table).insert(1, "u1", None, "p1")
print(sql)

sql = Query.into(table).insert((1, "u1", None, "p1"), (2, "u2", None, "p2"))
print(sql)

sql = (
    Query.into(table)
    .columns("id", table.field("name"), table.age, Field("place"))
    .insert(1, "u1", 16, "p1")
)
print(sql)
