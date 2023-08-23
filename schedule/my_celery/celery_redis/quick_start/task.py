import time
from celery import Celery

# 需要制定broker和backend两个

# broker 负责消息传输
# backend 用于储存执行结果
celery_app = Celery("hello", broker="redis://127.0.0.1:6379/1"
             ,backend="redis://127.0.0.1:6379/2",broker_connection_retry_on_startup=True)


@celery_app.task
def task(name, age):
    print("准备执行任务啦")
    time.sleep(5)
    return f"name is {name}, age is {age}"
