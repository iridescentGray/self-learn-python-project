from fastapi.background import P


class ForTest:
    field = "origin"

    def a_method(self):
        print("invoke ForTest.a_method")


def test_for_test(mocker):
    test = ForTest()
    mock_method = mocker.patch.object(test, "a_method")
    print(test.a_method)  # MagicMock name='a_method'
    test.a_method()
    print(mock_method.called)

    print(test.field)
    mocker.patch.object(test, "field", "mocked")
    print(test.field)
