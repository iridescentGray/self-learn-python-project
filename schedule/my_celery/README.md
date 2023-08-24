# celery

Distributed Task(Timing, Delay, Batch)

## use

### Used by pyenv virtualenv celery

    pyenv virtualenv  3.10.12 celery
    pyenv activate celery
    python -m pip install --upgrade pip
    cd schedule/celery
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    celery: https://github.com/celery/celery
    celery-doc: https://docs.celeryq.dev/en/stable/index.**html**

## project

### celery_redis

#### introduce

celery base on redis
Base on MacOs ,if you want to use windows run ,it need Specific parameters

#### quick_start

    # 通过注解配置celery任务

    # 进入目录
    cd schedule/my_celery/celery_redis/quick_start
    # 执行如下命令，创建一个worker，worker会等待获取任务执行
    celery  -A task  worker  -l  info

    -A参数：表示Celery对象所在的py文件的文件名，会自动记录task.py里面被@app.task装饰的函数
    -l参数：日志级别
    -c参数：表示并发数量，比如再加上-c 10，表示限制并发数量为10

    # 创建task，给worker可执行的任务，
    执行create_task_by_delay.py

    #如果修改了task，需要，那么重启celery worker才能生效

#### celery_from_config

    # 通过配置类配置celery
    # 进入目录
    cd schedule/my_celery/celery_redis/celery_from_config
    # 同时介绍了一些特殊的创建任务的办法(group+chain),还介绍了一些@app.task的参数

    # 创建worker
    celery  -A celery_app.app worker  -l  info

    # 创建task，给worker可执行的任务，
    执行 python create_task_by_delay.py

    # 创建group task，给worker可执行的任务，
    执行 python create_group_task.py 

    # 创建group task，给worker可执行的任务，
    执行 python create_chain_task.py

#### schedules

    # celery实现定时任务
    # 进入目录
    cd schedule/my_celery/celery_redis/schedules

    # 创建worker
    celery  -A celery_app.app worker  -l  info

    # 启动beat(用于create task)
    celery -A celery_app beat  -l info

    # 二合一命令：创建worker + 启动beat
    celery  -A celery_app worker  -B  -l info

    # 后台启动celery worker进程
    celery -A celery_app multi start work_1 

    # 查看进程数
    celery -A celery_app status

## uninstall

    pyenv virtualenv-delete celery
