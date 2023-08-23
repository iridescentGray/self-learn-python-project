broker_url = "redis://127.0.0.1:6379/1"
result_backend = "redis://127.0.0.1:6379/2"
broker_connection_retry_on_startup = True
timezone = "Asia/Shanghai"
CELERY_ENABLE_UTC = False


from celery.schedules import crontab
from datetime import timedelta


# 导入任务所在文件
imports = ["task"]

# 需要执行任务的配置
beat_schedule = {
    "schedule_task1": {
        # 具体需要执行的函数
        # 该函数必须要使用@app.task装饰
        "task": "task.task1",
        # 定时时间
        # 每分钟执行一次，不能为小数
        "schedule": crontab(minute="*/1"),
        # 或者这么写，每小时执行一次
        # "schedule": crontab(minute=0, hour="*/1")
        # 执行的函数需要的参数
        "args": (),
    },
    "schedule_task2": {
        "task": "task.task2",
        # 设置定时的时间，5秒一次
        "schedule": timedelta(seconds=5),
        "args": ("test_name",),
    },
}
