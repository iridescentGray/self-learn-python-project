i = 1
f = None
or_sugar_i = i or 0  # 1
or_sugar_f = f or 0  #

or_sugar_dict = f or {}  #

print(or_sugar_i)
print(or_sugar_f)

print(or_sugar_dict)

tuple_args = (1,)
tuple_args = tuple(tuple_args or ())
print(tuple_args)
