import celery_config as celery_config
from celery import Celery

app = Celery(__name__, include=["task"])
# 通过加载配置文件的方式制定
app.config_from_object(celery_config)
