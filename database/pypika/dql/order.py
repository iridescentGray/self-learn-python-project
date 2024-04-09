from pypika import Order, Query

sql = Query.from_("t").select("id", "name").orderby("id", order=Order.desc)
print(sql)

sql = Query.from_("t").select("id", "name").orderby("age", "id")
print(sql)

sql = Query.from_("t").select("id", "name").orderby("age", "id", order=Order.desc)
print(sql)

sql = (
    Query.from_("t").select("id", "name").orderby("age", order=Order.desc).orderby("id")
)
print(sql)
