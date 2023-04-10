# django

django相关demo

## 环境搭建

### 通过pyenv的virtualenv插件使用

    pyenv virtualenv  3.10.9 my-django  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate my-django
    python -m pip install --upgrade pip
    cd web_framework/mydjango/ 
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## 项目

### restapi_demo

#### 项目介绍

restapi_demo是一个使用了django+djangorestframework+redis的简单样例项目，让django能够提供RestFul风格的API。

#### 相关文档
    django： https://docs.djangoproject.com/zh-hans/4.2/
    djangorestframework：https://www.django-rest-framework.org/    
    redis：  https://django-redis-chs.readthedocs.io/zh_CN/latest/ 
    

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
 

