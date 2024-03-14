import pytest


def string_upper(s: str) -> str:
    """将某个字符串里的所有英文字母,由小写转换为大写"""
    chars = []
    for ch in s:
        if "a" <= ch <= "z":
            # 32 是小写字母与大写字母在 ASCII 码表中相差的距离
            chars.append(chr(ord(ch) - 32))
        else:
            chars.append(ch)
    return "".join(chars)


# 这段测试较为复杂,可以被下面的pytest.mark.parametrize 完全替代
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
