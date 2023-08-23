from celery_app import app


@app.task
def task1():
    print("我是task1")
    return "task1你好"


@app.task
def task2(name):
    print(f"我是{name}")
    return f"{name}你好"


@app.task
def task3():
    print("我是task3")
    return "task3你好"


@app.task
def task4(name):
    print(f"我是{name}")
    return f"{name}你好"
