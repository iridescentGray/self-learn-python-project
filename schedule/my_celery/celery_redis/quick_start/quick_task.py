import time 
from quick_task import task

# 导入task, 创建任务
# 但是注意: 不要直接调用task, 因为那样的话就在本地执行了
# 我们的目的是将任务发送到队列里面去, 然后让监听队列的worker从队列里面取任务并执行
# 而task是被@app.task装饰了, 所以它不在是原来的task了, 我们需要调用它的delay方法


# 调用delay之后, 就会创建一个任务, 然后发送到队列里面去, 也就是我们这里的Redis
# 至于参数, 普通调用的时候怎么传, 在delay里面依旧怎么传
start = time.perf_counter()
task.delay()
print(time.perf_counter() - start)  # 0.5087445999999999