import datetime


dt1 = datetime.datetime(2023, 1, 1)
dt2 = datetime.datetime(year=2023, month=1, day=1, hour=12, minute=30, second=15)

print(type(dt1), dt1)
print(dt2.hour, dt2.month)
