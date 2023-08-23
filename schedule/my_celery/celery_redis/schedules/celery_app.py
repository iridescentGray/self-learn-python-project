from celery import Celery
import celery_config as celery_config

app = Celery(__name__,include=["task"])
# 通过加载配置文件的方式制定
app.config_from_object(celery_config)