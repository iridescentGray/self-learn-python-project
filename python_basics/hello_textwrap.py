import textwrap

"""
 textwrap 用于格式化要输出的文本,实现美观打印(pretty-printing)

"""
text = """
    There are moments in life when you miss someone
    so much that you just want to pick them
    from your dreams and hug them for real! Dream what
    you want to dream;go where you want to go;
    be what you want to be,because you have
    only one life and one chance to do all the things you want to do.
"""

print("----------------------------fill------------------------------")

# fill取文本作为输入,生成格式化文本输出
# width 限制每行宽度为50
print(textwrap.fill(text, width=50))  # 结果不是太让人满意。文本虽然已经对齐,不过只有第一行保留了缩进

print("----------------------------dedent------------------------------")

print(textwrap.dedent(text).strip())  # dedent可以去除空白符,会生成更好的结果

print("----------------------------fill+dedent------------------------------")
# 限制每行宽度+去空格,效果不错
dedent_text = textwrap.dedent(text).strip()
print(textwrap.fill(dedent_text, width=60))  # 先去除缩进,然后填充,每行长度60个字符

print(
    "----------------------------fill+dedent subsequent_indent------------------------------"
)
# 悬挂缩进
print(
    textwrap.fill(dedent_text, initial_indent="", subsequent_indent=" " * 4, width=50)
)

print(
    "----------------------------fill+dedent subsequent_indent------------------------------"
)
# 悬挂缩进+填充缩进字符
print(
    textwrap.fill(
        dedent_text,
        initial_indent="",  # 首行缩进
        subsequent_indent="*" * 4,  # 首行之外的行缩进
        width=50,
    )
)

print("----------------------------indent------------------------------")
final_text = textwrap.indent(dedent_text, ">>>")  # 为一个字符串的所有行增加一致的前缀文本
print(final_text)

print(
    "----------------------------indent_for_target_line------------------------------"
)

# 文本长度大于40的，增加一致的前缀文本
final_text = textwrap.indent(
    dedent_text, prefix=" -> ", predicate=lambda line: len(line.strip()) > 40
)
print(final_text)


print("----------------------------shorten------------------------------")
# 省略50字符以后的文本
print(textwrap.shorten(dedent_text, width=50))
