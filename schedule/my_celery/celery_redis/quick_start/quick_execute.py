from celery import Celery

app = Celery('hello', broker='redis://127.0.0.1:6379/1')

@app.task
def hello():
    return 'hello world'