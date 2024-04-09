from prettytable import from_csv

print(
    "\n---------------------------------read from csv---------------------------------------\n"
)
with open("./test.csv") as f:
    tb = from_csv(f)
    print(tb)
