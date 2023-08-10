from xpinyin import Pinyin

# 实例化Pinyin这个类
p = Pinyin()

# 传入汉字，直接返回拼音
print(p.get_pinyin("测试人名"))

# 默认拼音之间是以"-"进行相连的，我们也可以自己指定
print(p.get_pinyin("测试人名", splitter=" "))
# 还可以返回声调
print(p.get_pinyin("测试人名", splitter=" ", tone_marks="marks"))
# gu后面的3就表示3声
print(p.get_pinyin("测试人名", splitter=" ", tone_marks="numbers"))

# 可以将内容转为大写，默认是小写
print(p.get_pinyin("测试人名", splitter=" ", convert="upper"))
# 首字母大写
print(p.get_pinyin("测试人名", splitter=" ", convert="capitalize"))

# 还可以获取拼音的首字母
print(p.get_initials("测试人名"))
print(p.get_initials("测试人名", " "))
