from dateutil import rrule, parser

# 生成时间跨度

print(
    list(
        rrule.rrule(
            freq=rrule.DAILY,
            dtstart=parser.parse("2018-1-1"),
            until=parser.parse("2018-1-5"),
        )
    )
)


time_interval_day = rrule.rrule(
    freq=rrule.DAILY, dtstart=parser.parse("2018-1-1"), until=parser.parse("2019-1-5")
).count()
print(f"time_interval_day :{time_interval_day}")

time_interval_year = rrule.rrule(
    freq=rrule.YEARLY, dtstart=parser.parse("2018-1-1"), until=parser.parse("2019-1-5")
).count()
print(f"time_interval_year :{time_interval_year}")
