import os


def test_mocker_patch(mocker):
    filename = "test.file"
    # 创建假的os.remove,并不会真正执行remove
    print(type(os.remove))  # builtin_function_or_method
    mocker.patch("os.remove")
    print(type(os.remove))  # unittest.mock.MagicMock

    # 即使并没有test.file,也不会报错，因为os.remove是一个MagicMock
    os.remove(filename)
