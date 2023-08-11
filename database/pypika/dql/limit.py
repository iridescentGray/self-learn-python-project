from pypika import Query, Table

table = Table("t")
print(Query.from_(table).distinct().select(table.id, table.age))
