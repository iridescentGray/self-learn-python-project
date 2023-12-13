# sqlite

sqlite database

## use

### Used by pyenv virtualenv sqlite

    pyenv virtualenv  3.11.6 sqlite
    pyenv activate sqlite
    python -m pip install --upgrade pip
    cd database/sqlite
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    sqlite: https://github.com/sqlite/sqlite
    sqlite-python: https://docs.python.org/zh-cn/3/library/sqlite3.html

## uninstall

    pyenv virtualenv-delete sqlite
