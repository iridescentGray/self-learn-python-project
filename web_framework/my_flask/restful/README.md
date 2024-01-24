
# start-up

## 方法1
    flask run


## 方法2
    python run.py

# init database
    # 第一次初始化时使用
    flask db init
    # 后面每次修改数据库字段时使用
    flask db migrate
    flask db upgrade


### docker run
    # build image
    docker build -t flask_service_image .
    # 启动
    docker run -d --restart=always -p 5000:5000 flask_service_image
