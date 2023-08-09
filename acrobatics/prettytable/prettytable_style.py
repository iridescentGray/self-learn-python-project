from prettytable import PrettyTable
import prettytable

x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])

x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])


print(
    "-----------------------------------------set_style-----------------------------------------------\n"
)
x.set_style(prettytable.MSWORD_FRIENDLY)
print(x)


# 是否显示边框，默认为True
x.border = True
# 横边框
x.horizontal_char = "^"
# 竖边框
x.vertical_char = ">"
# 边框连接符
x.junction_char = "~"

print(x)
