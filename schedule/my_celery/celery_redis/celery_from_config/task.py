from celery import Task
from celery_app import app

"""
@app.task的参数:

name:默认的任务名是一个uuid,我们可以通过name参数指定任务名,当然这个name就是apply_async中的name,如果在apply_async中指定了,那么以apply_async中指定的为准。

bind:一个bool值,表示是否绑定一个task的实例,如果绑定,task实例会作为参数传递到任务方法中,可以访问task实例的所有属性。

base:定义任务的基类,用于定义回调函数,当任务到达某个状态时触发不同的回调函数,默认是Task,所以我们一般会自己写一个类然后继承Task。

default_retry_delay:设置该任务重试的延迟机制,当任务执行失败后,会自动重试,单位是秒,默认是3分钟。

serializer:指定序列化的方法。

"""


@app.task(name="test_task_name")
def add(x, y):
    return x + y


@app.task
def sub(x, y):
    return x - y


@app.task(name="i_am_bind", bind=True)
def bind_test(self, a, b):
    print("bind_test self:", self)
    # self.request存储了相应的属性
    print("bind_test self.request:", self.request)
    # 获取name
    print("bind_test name:", self.name)
    return f"a - b = {a - b}"


class MyTask(Task):
    """自定义一个类，继承自celery.Task"""

    """
    exc:失败时的错误的类型；
    task_id:任务的id；
    args:任务函数的参数；
    kwargs:参数；
    einfo:失败时的异常详细信息；
    retval:任务成功执行的返回值；
    """

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """任务失败时执行"""

    def on_success(self, retval, task_id, args, kwargs):
        print("base_callback-任务执行成功")

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """任务重试时执行"""


@app.task(name="base_callback", base=MyTask)
def base_callback(x, y):
    print("base_callback 加法计算")
    return x + y
