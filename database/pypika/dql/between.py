from pypika import Field, Query, Table

girl = Table("girl")

sql = Query.from_(girl).select("*").where(Field("age").between(18, 30))
print(sql)

sql = (
    Query.from_(girl)
    .select("*")
    .where(Field("age")[18:30])
    .where(Field("length").isin([155, 156, 157]))
)
print(sql)
