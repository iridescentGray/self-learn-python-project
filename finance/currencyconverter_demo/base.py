from datetime import date

from currency_converter import CurrencyConverter

c = CurrencyConverter()

print(c.convert(1, "USD", "CNY"))
print(c.convert(1, "USD", "CNY", date=date(2024, 1, 11)))
print(c.bounds["CNY"])
