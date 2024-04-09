from pypika import Query, Table
from pypika import functions as fn

table1 = Table("t1")
table2 = Table("t2")

sub_query = (
    Query.from_(table1)
    .select(fn.Avg(table2.age).as_("avg"))
    .left_join(table2)
    .on(table1.field("uid") == table2.field("tid"))
    .where(table1.age > 18)
)
print(sub_query)


sql = Query.from_(sub_query).select("avg")
print(sql)
