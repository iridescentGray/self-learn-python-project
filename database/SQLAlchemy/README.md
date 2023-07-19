# SQLAlchemy

SQLAlchemy,database orm framework

## Environmental construction

### Used by pyenv virtualenv plugin

    工具
    pyenv virtualenv  3.10.9 SQLAlchemy
    pyenv activate SQLAlchemy
    python -m pip install --upgrade pip
    cd database/SQLAlchemy
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    SQLAlchemy：https://www.sqlalchemy.org/

## project

### asyncio_mysql_demo

#### introduce

use asyncio to control mysql
Warning: asyncio MySQL is unstable,don't use in prod

#### start-up
    execute 'database/SQLAlchemy/asyncio_mysql_demo/demo.sql' in mysql

## uninstall

    pyenv virtualenv-delete SQLAlchemy