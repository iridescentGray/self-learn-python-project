import os

from fastapi.background import P


def test_spy_listdir(mocker):
    mock_listdir = mocker.spy(os, "listdir")
    print(os.listdir)
    print(os.listdir())
    print(mock_listdir.called)
