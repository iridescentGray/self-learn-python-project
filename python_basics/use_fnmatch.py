import fnmatch
import os

"""
fnmatch是用来匹配字符串/文件名(通过glob模式、如Unix shell所使用的的模式)
在一些匹配不是很复杂的情况下，可以使用 fnmatch 来替代正则表达式

规则:
?:匹配一个任意字符
*:匹配任意个任意字符
[sequence]:匹配出现在sequence里面的一个字符
[!sequence]:匹配没有出现在sequence里面的一个字符
[a-m]:匹配出现在abcdef...m中的字符
[A-M]:匹配出现在ABCDEF...M中的字符
[0-9]:匹配出现在0123...9中的字符
"""
print("----------------------------Base Usege------------------------------")

print(fnmatch.fnmatch("abcde", "*"))  # True
print(fnmatch.fnmatch("abcde", "abc?"))  # False
print(fnmatch.fnmatch("abcde", "abc??"))  # True
print(fnmatch.fnmatch("abcde", "[a-z]????"))  # True
print(fnmatch.fnmatch("aaa", "aaa*"))  # True
print(fnmatch.fnmatch("1ab", "[0-1]??"))  # True

# 注意fnmatch会是用os.path.normcase("A"),解析字符串，大小写敏感难以确定
print(fnmatch.fnmatch("Aaa", "aaa"))  # False
# 如果我想区分大小写呢？可以使用fnmatchcase
print(fnmatch.fnmatchcase("Aaa", "aaa"))  # False

print("----------------------------list and match------------------------------")

for name in os.listdir(r"./python_basics"):
    if fnmatch.fnmatch(name, "use_*.py"):
        print(f"listdir fnmatch use_*.py: {name}")

print("----------------------------usr filter------------------------------")

print(f'use filter:  {fnmatch.filter(os.listdir(r"./python_basics"), "use_*.py")}')

print("----------------------------glob 模式转换为正则表达式------------------------------")

pattern = "use_*.py"
print(fnmatch.translate(pattern))  # (?s:use_.*\.py)\Z
