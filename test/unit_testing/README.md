# unit_testing

单元测试相关demo

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 unit_testing  //此外，还需要使用编译器的Add Interpreter功能把这个虚拟环境识别了
    pyenv activate unit_testing
    python -m pip install --upgrade pip
    cd test/unit_testing
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/


## project

### mypytest

#### Project Introduction

mypytest是一个pytest项目
pytest是一个开源的第三方单元测试框架，第一个版本发布于2009年。
pytest功能多，设计复杂，但pytest的最大优势在于，它把Python的一些惯用写法与单元测试很好地融合了起来。

#### Related documents

    pytest git： https://github.com/pytest-dev/pytest
    pytest-doc： https://docs.pytest.org/en/stable/
