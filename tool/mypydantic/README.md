# pydantic

pydantic是使用Python类型注释，进行数据验证和设置管理的工具 值得一提的是，pydantic的类对json转化友好，无需定义Serializer

## Environmental construction

### Used by pyenv virtualenv plugin

    工具
    pyenv virtualenv  3.10.9 my-pydantic
    pyenv activate my-pydantic
    python -m pip install --upgrade pip
    cd tool/mypydantic
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## uninstall

    pyenv virtualenv-delete my-pydantic