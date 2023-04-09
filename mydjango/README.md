# django

django相关demo

## 环境搭建

### 通过pyenv的virtualenv插件使用

    pyenv virtualenv  3.10.9 my-django
    pyenv activate my-django
    python -m pip install --upgrade pip
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## 启动项目

### restapi_demo

#### 启动项目

    cd restapi_demo                   //进入项目目录
    python manage.py migrate          //初始化数据库，默认sqlite3使用
    python manage.py createsuperuser  //初始化超级管理员
    python manage.py runserver        //启动服务

#### 测试接口

    http://127.0.0.1:8000/admin                          //打开管理员界面，密码由createsuperuser命令制定
    http://127.0.0.1:8000/rest-api/show_people           //测试接口1调用
    http://127.0.0.1:8000/rest-api/show_teachers/?sno=1  //测试接口2调用
    http://127.0.0.1:8000/rest-api/show_subjects/        //测试接口3调用
    http://127.0.0.1:8000/rest-api/subjects/             //测试CBV视图提供的列表接口4调用

## 卸载项目

    pyenv virtualenv-delete my-django
 

