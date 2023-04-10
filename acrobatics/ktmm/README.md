# ktmm

## 介绍

ktmm是一个通过移动鼠标防止系统休眠的脚本。

- 原始项目：https://github.com/ao/ktmm

## 使用

### 通过pyenv的virtualenv插件使用

    pyenv virtualenv  3.9.16 ktmm
    pyenv activate ktmm
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
    cd acrobatics/ktmm/
    python ktmm.py

### 卸载

    pyenv virtualenv-delete ktmm