# django

django相关demo

## 使用

### 通过pyenv的virtualenv插件使用

    pyenv virtualenv  3.10.9 my-django
    pyenv activate my-django
    python -m pip install --upgrade pip
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### 启动项目

#### restapi_demo的启动

    cd restapi_demo                   //进入项目目录
    python manage.py migrate          //初始化数据库，默认sqlite3使用
    python manage.py createsuperuser  //初始化超级管理员
    python manage.py runserver        //启动服务

    http://127.0.0.1:8000/admin                   //管理员界面
    http://127.0.0.1:8000/rest-api/show_people    //测试接口调用
    


### 卸载

    pyenv virtualenv-delete my-django
 

