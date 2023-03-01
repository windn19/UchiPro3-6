import datetime


date = datetime.datetime(2023, 1, 1)
now = datetime.datetime.now()
delta = now - date

print(type(delta))
print(delta)
print(delta.days, delta.seconds)
