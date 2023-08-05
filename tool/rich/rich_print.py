from rich import print


print("[blue]少女惧怕幽灵")

print("[bold]粗体")

print("[bold red]红色粗体")
print("[italic red]italic red")
print("[underline red]红色下划线")
print("[bold italic underline red]加粗、下划线、红色")

#不同部分，不同的颜色、属性
print("[italic bold red]komeiji  [cyan bold]satori")

# 只对字符串的某一部分,类似html，需要一个闭合标签
print("[italic bold red]komeiji[/italic bold red]  satori")

# auto format
print({i: f"satori_{i}" for i in range(1, 10)})