import os


def test_return_value(mocker):
    """修改被patch对象的返回值"""
    isfile = mocker.patch("os.path.isfile", return_value=True)
    print(isfile)
    print(os.path.isfile("test"))


def test_side_effect(mocker):
    """让被patch的对象抛出异常"""
    isfile = mocker.patch("os.path.isfile", side_effect=TypeError)
    print(isfile)
    print(os.path.isfile("test"))
