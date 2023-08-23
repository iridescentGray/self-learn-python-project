# docker

Docker SDK

## use

### Used by pyenv virtualenv docker

    pyenv virtualenv  3.10.12 docker
    pyenv activate docker
    python -m pip install --upgrade pip
    cd cloud/my_docker
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    docker-sdk: https://github.com/docker-library/python
    docker-sdk-doc: https://docker-py.readthedocs.io/en/stable/index.html

## uninstall

    pyenv virtualenv-delete docker
