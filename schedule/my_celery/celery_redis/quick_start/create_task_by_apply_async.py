from task import task

# task.delay实际上调用了task.apply_async
# delay只接收函数的参数，apply_async接收的参数更多
print(task.apply_async([1,2], task_id="this_is_my_apply_async_task", countdown=3).get())  # 3

# countdown： 倒计时，表示多少秒后执行，参数为整型
