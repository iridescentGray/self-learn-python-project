# ktmm

## introduce

Ktmm is a script that prevents system hibernation by moving the mouse。

- Original project：https://github.com/ao/ktmm

## use

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.9.16 ktmm
    pyenv activate ktmm
    python -m pip install --upgrade pip
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
    cd acrobatics/ktmm/
    python ktmm.py

### uninstall

    pyenv virtualenv-delete ktmm
