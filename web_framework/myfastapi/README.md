# FastAPI

FastAPI相关demo
FastAPI 是一个用于构建API（网络数据接口）的现代、高性能的Web框架，基于Python 3.6+， 使用了Python中的类型提示进行类型检查，非常符合工程化开发的需求，在业界有非常好的口碑。

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 my-fastapi  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate my-fastapi
    python -m pip install --upgrade pip
    cd web_framework/myfastapi/
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    FastAPI： https://fastapi.tiangolo.com/zh/
    pydantic：https://docs.pydantic.dev/
    starlette：https://www.starlette.io/

## project

### fastapi_demo

#### introduce

fastapi_demo是一个使用了fast-api的简单样例项目

#### start-up

    cd fastapi_demo
    uvicorn main:app --reload
    查看项目接口文档： http://127.0.0.1:8000/docs
    另一种接口文档：http://127.0.0.1:8000/redoc

#### Test interface

    http://127.0.0.1:8000/

## uninstall

    pyenv virtualenv-delete my-fastapi
