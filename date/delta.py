import datetime

date = datetime.datetime(2022, 12, 31)
delta = datetime.timedelta(days=3)
new_date = date - delta


print(type(delta), delta)
print(new_date)
