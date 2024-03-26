import os


def test_spy_listdir(mocker):
    """spy: 用MagicMock包装,而不改变其功能
    可以跟踪函数/方法调用、返回值和引发的异常

    """
    mock_listdir = mocker.spy(os, "listdir")
    print(os.listdir)
    print(os.listdir())
    print(mock_listdir.called)
