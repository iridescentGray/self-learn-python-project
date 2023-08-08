from thefuzz import process

words = ["hello python", "hello java", "hello golang", "hello php"]
# 会自动和words里面的每一个元素进行比较，然后按照相似度从高到低排列
print(process.extract("hello thon", words))
# [('hello python', 91), ('hello php', 74), ('hello golang', 73), ('hello java', 64)]

# 还可以传入一个limit参数，表示只返回前limit个，默认为5
print(
    process.extract("hello thon", words, limit=2)
)  # [('hello python', 91), ('hello php', 74)]

# 返回分数最高的
print(process.extractOne("hello thon", words))  # ('hello python', 91)
