from pypika import Database, Query, Table

print(
    f"------------------------------------------must declare table-----------------------------------------"
)

db = Database("my_db")

table = db.user
sql = Query.from_(table).select(table.id)
print(sql)  # SELECT "id" FROM "my_db"."my_schema"."t"
