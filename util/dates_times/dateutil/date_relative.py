from datetime import datetime

from dateutil.relativedelta import relativedelta

print("------------------用于计算两个日期之间的差值,但不够好用----------------")


print(
    relativedelta(datetime(2018, 1, 5), datetime(2018, 1, 1))
)  # relativedelta(days=+4)

print(
    relativedelta(datetime(2018, 2, 5), datetime(2018, 1, 9))
)  # relativedelta(days=+27)

print(
    relativedelta(datetime(2018, 2, 5), datetime(2018, 1, 1))
)  # relativedelta(months=+1, days=+4)

print(
    relativedelta(datetime(2019, 2, 5), datetime(2018, 1, 1))
)  # relativedelta(years=+1, months=+1, days=+4)

print("-------------------------------diff------------------------------------")

dt1 = datetime(2018, 12, 11, 19, 15, 25)
dt2 = datetime(2017, 8, 3, 17, 24, 51)

diff = relativedelta(dt1, dt2)
print(diff)

print(diff.years)  # 1
print(diff.months)  # 4
print(diff.days)  # 8

print(diff.hours)  # 1
print(diff.minutes)  # 50
print(diff.seconds)  # 34

print("--------------------------用于时间偏移，不错----------------------------")
dt3 = datetime(2018, 12, 11, 19, 15, 25)

# 加5个月，变成了19年5五月
dt_deviation = relativedelta(months=5)
print(dt3 + dt_deviation)  # 2019-05-11 19:15:25
