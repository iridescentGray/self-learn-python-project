# smalltool_collection

工具集合

## 使用

### 通过pyenv的virtualenv插件使用

    工具
    pyenv virtualenv  3.10.9 smalltool_collection
    pyenv activate smalltool_collection
    python -m pip install --upgrade pip
    cd tool/smalltool_collection
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## 包含

- cache：缓存模块
  - cachetools：python缓存第三方工具
      - 文档：https://cachetools.readthedocs.io/en/latest/