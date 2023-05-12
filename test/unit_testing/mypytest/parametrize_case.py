import pytest

from test_method import string_upper


# 这段测试较为复杂，可以被下面的pytest.mark.parametrize 完全替代
# def test_string_upper():
#     assert string_upper('foo') == 'FOO'
#
# def test_string_empty(): <.>
#     assert string_upper('') == ''
#
# def test_string_mixed_cases():
#     assert string_upper('foo BAR') == 'FOO BAR'


# 表驱动测试
@pytest.mark.parametrize(
    # 参数名称
    "s,expected",
    # 参数内容
    [
        ("foo", "FOO"),
        ("", ""),
        ("foo BAR", "FOO BAR"),
    ],
)
def test_string_upper(s, expected):
    assert string_upper(s) == expected
