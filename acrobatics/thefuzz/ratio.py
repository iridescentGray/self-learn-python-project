from thefuzz import fuzz

# fuzz.ratio即可计算两个字符串之间的相似度
print(fuzz.ratio("this is a test", "this is a test!"))  # 97

# partial_ratio是非完全匹配，如果一方结束了，那么剩下的就不考虑了
print(fuzz.partial_ratio("this is a test", "this is a test!"))  # 100

# token_sort_ratio表示忽略顺序匹配，但前提是多个词，以空格进行分隔。所以明显是针对英文的
print(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))  # 91
print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))  # 100


# token_set_ratio表示去重匹配，同样：前提是多个词，以空格进行分隔
print(fuzz.token_sort_ratio("fuzzy was a bear", "wuzzy fuzzy was a bear"))  # 84
print(
    fuzz.partial_token_sort_ratio("fuzzy was a bear", "wuzzy fuzzy was a bear")
)  # 100
