
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
    docker build --no-cache -t flask_service_image .
    # 启动
    docker run -d --restart=always -p 5000:5000 flask_service_image


# http request

## /api/register

    curl --location --request POST 'http://localhost:5000/api/register' \
    --header 'Content-Type: application/json' \
    --header 'Accept: */*' \
    --header 'Host: localhost:5000' \
    --data-raw '{
        "username": "root",
        "pwd": "123456"
    }'

## /api/login

    curl --location --request POST 'http://localhost:5000/api/login' \
    --header 'Content-Type: application/json' \
    --header 'Accept: */*' \
    --header 'Host: localhost:5000' \
    --header 'Connection: keep-alive' \
    --data-raw '{
        "username": "root",
        "pwd": "123456"
    }'


## /api/getUserList
    curl --location --request GET 'http://localhost:5000/api/getUserList' \
    --header 'Authorization: Bearer ' \
    --header 'Content-Type: application/json' \
    --header 'Accept: */*' \
    --header 'Host: localhost:5000' \
    --header 'Connection: keep-alive' \
    --data-raw ''

## /api/getUserList
    curl --location --request POST 'http://localhost:5000/api/logout' \
    --header 'Authorization: Bearer ' \
    --header 'Content-Type: application/json' \
    --header 'Accept: */*' \
    --header 'Host: localhost:5000' \
    --header 'Connection: keep-alive' \
    --data-raw ''