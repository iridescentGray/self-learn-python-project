from task import task

# 但是注意: , 因为那样的话就在本地执行了

# 不要直接调用task，而是调用task的delay方法, delay方法会创建一个任务, 发送到Redis里面去
# 参数可以和普通调用时一样
t = task.delay("test", "16")

print(type(t))  # <class 'celery.result.AsyncResult'>
print(t)  # 直接打印, 显示的是任务的id 29e8e2e5-baca-4f64-bb40-a7dc0f8dd385
print(t.status)  ## 获取状态，没有执行完, 因此结果是PENDING
# 获取id, 可以调用task_id或者id
print(t.task_id, t.id)  # 两者效果一致
print(t.date_done)  # 获取任务执行结束时的时间，如果没有结束, 所以返回None

# 查看任务状态，任务执行完成返回True，否则为False
print(f"t.ready() {t.ready()}")  # 只要任务没有处于阻塞状态就会返回True, 比如执行成功、执行失败
print(f"t.successful() {t.successful()}")  # 在任务执行成功后返回True, 否则返回False


# 获取任务的返回值, 可以通过result或者get()
print(t.result)  # result()在任务还没有执行完时，会直接返回None
print(t.get())  # get()会阻塞直到任务完成

# 再次查看状态和执行时间
print(f"t.status  {t.status}")  
print(f"t.date_done  {t.date_done}") 

# 查看任务状态，任务执行完成返回True，否则为False
print(f"t.ready()  {t.ready()}")  # 只要任务没有处于阻塞状态就会返回True, 比如执行成功、执行失败
print(f"t.successful()  {t.successful()}")  # 在任务执行成功后返回True, 否则返回False

# 如果任务抛出了一个异常，可以获取原始的回溯信息
print(t.traceback)  # None
