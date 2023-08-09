# redis

not say more

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 redis
    pyenv activate redis
    python -m pip install --upgrade pip
    cd database/redis
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    redis： https://redis.io/
    redis-py： https://github.com/redis/redis-py
    redis-py-doc： https://redis.readthedocs.io/en/stable/examples.html
    rq: https://python-rq.org/docs/

## project

### redispy_demo

#### introduce

python redis Introduction to Operation Cases

#### start-up

### rq_demo

#### introduce

rq_demo is a demo for rq library. rq is a simple library for queueing jobs and processing them in the background with
workers.

#### start-up

## uninstall

    pyenv virtualenv-delete redis