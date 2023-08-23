from task import add, sub,bind_test,base_callback

print(add.delay(2, 3).get())  # 5
print(sub.delay(3, 2).get())  # 1
print(bind_test.delay(3, 2).get())  # a - b = 1
print(bind_test.delay(3, 2).get())  # a - b = 1
print(base_callback.delay(3, 2).get())  # 5