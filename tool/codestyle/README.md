# codestyle

codestyle,此模块中的工具用于：让团队代码风格一致，符合规范

## 使用

### Used by pyenv virtualenv plugin
    工具
    pyenv virtualenv  3.10.9 codestyle
    pyenv activate codestyle
    python -m pip install --upgrade pip
    cd tool/codestyle
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## 规范工具
- pre-commit ———— 基于githooks的代码规范检查平台
- black ———— 代码强制格式化
- isort ———— 导包排序排序


### pre-commit
#### introduce
    pre-commit 在每一次commit前自动进行代码检查和格式化，
    如果pre-commit返回了错误状态码，则该次提交将不能通过。
    幸运的是，当前流行的一个使用Python编写的同名工具 pre-commit，
    使得只需要在项目根目录下添加一个.pre-commit-config.yaml文件并写上相应的配置即可整合很多代码检查和格式化工具，
    实现自动代码检查和格式化。
#### 命令
    # 初始化 pre-commit,pre-commit利用了git的hook机制，会在git commit前，插入自己的操作
    pre-commit install   # console output: pre-commit installed at .git/hooks/pre-commit
    #（可选）创建一个.pre-commit-config.yaml 文件：通过官方cli工具 ，或直接复制本项目的.pre-commit-config.yaml
    pre-commit sample-config > .pre-commit-config.yaml
    # 用pre-commit检查所有git文件
    pre-commit
    # 用pre-commit检查并修改所有git文件
    pre-commit run --all-files

### black
    用于代码强制格式化
    ps：引号使用双引号

### isort

####introduce
    用于给包导入按照如下顺序排序：
    （1）导入Python标准库包的import语句；
    （2）导入相关联的第三方包的import语句；
    （3）与当前应用（或当前库）相关的import语句。


## uninstall

    pyenv virtualenv-delete codestyle