import datetime


time1 = datetime.datetime.now().time()
time2 = datetime.time(hour=15, minute=30, second=23)

print(type(time1), time1)
print(type(time2), time2)
print(time2.hour, time2.minute, time2.second)
