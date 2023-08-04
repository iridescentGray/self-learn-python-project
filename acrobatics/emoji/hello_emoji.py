import emoji

print("-------------------------------parsing code------------------------------------")
print(chr(127825))  # 🍑
peach: int = ord("🍑")
print(f"peach code is {peach}")


print(
    "----------------------------Forward parsing phrase------------------------------"
)
emoji_grammar = emoji.emojize(f"emoji_grammar_test: 你在想 :peach: 吃")
print(emoji_grammar)

print("*" * 80)
print(emoji.emojize(":dromedary_camel:"))  # :dromedary_camel:
print(emoji.emojize(":dromedary_camel:", language="alias"))  # :dromedary_camel:

print("*" * 80)
print(emoji.emojize(":shit:", language="alias"))  # 💩
print(emoji.emojize("@@shit@@", delimiters=("@@", "@@")))  # @@shit@@
print(emoji.emojize("@@shit@@", delimiters=("@@", "@@"), language="alias"))  # 💩


print(
    "-------------------------------Reverse parsing phrase------------------------------------"
)
print(emoji.demojize("你在想 🍑 吃"))
print(emoji.demojize("你在想 💩 "))
