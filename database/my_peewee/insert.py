import peewee
from connection import db
from model import Girl

# 增加记录有以下几种方式
g1: Girl = Girl()

g1.name = "u1"
g1.where = "p1"

# 或者
g2 = Girl(name="u2", where="p2")

# 然后一定要save，否则记录不会进入到表中
g1.save()
g2.save()
Girl.create(name="u3", where="p3]")
