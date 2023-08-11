from pypika import Query, Field, Table, Criterion

girl = Table("girl")

sql = Query.from_(girl).select("*").where((Field("age") > 18) & Field("length") < 160)
print(sql)

sql = Query.from_(girl).select("*").where((Field("age") > 18) | Field("length") < 160)
print(sql)

sql = Query.from_(girl).select("*").where((Field("age") > 18) ^ Field("length") < 160)
print(sql)

sql = (
    Query.from_(girl)
    .select("*")
    .where(
        Criterion.all(
            [Field("id") > 10, Field("age") > 18, Field("length").isin([155, 156, 157])]
        )
    )
)
print(sql)

sql = (
    Query.from_(girl)
    .select("*")
    .where(
        Criterion.any(
            [
                Field("id").between(10, 50),
                Field("age") > 18,
                Field("length").isin([155, 156, 157]),
            ]
        )
    )
)
print(sql)
