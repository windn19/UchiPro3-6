import datetime


date = datetime.date.fromtimestamp(1672520400)
print(date)
d = datetime.datetime.timestamp(datetime.datetime.now())
print(d)
print(datetime.datetime.fromtimestamp(d))
