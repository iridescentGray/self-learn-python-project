from pypika import Field, Query, Table

girl = Table("girl")

sql = Query.from_(girl).select("*").where(Field("age") >= 18)
print(sql)

sql = (
    Query.from_(girl)
    .select("id")
    .select(girl.name)
    .select(Field("age"))
    .where(Field("age") >= 18)
    .where(girl.age <= 30)
    .where(Field("length") < 165)
)
print(sql)
