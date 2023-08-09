from re import T
from prettytable import PrettyTable, from_csv
import prettytable


print(
    "---------------------------------base useage---------------------------------------"
)
x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])

x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

x.add_column("additional_column", ["1"] * 7)

print(x)

print(
    "---------------------------------get specify position---------------------------------------"
)
print(x.get_string(fields=["City name"], start=1, end=3))

print(
    "-----------------------------------------sort-----------------------------------------------"
)
print(x.get_string(sortby="Population", reversesort=True))


print(
    "-----------------------------------------set alignment-----------------------------------------------"
)
# l代表左对齐，c代表居中，r代表右对齐
x.align["additional_column"] = "l"
x.align["Area"] = "c"
x.align["Annual Rainfall"] = "r"
