import datetime


now = datetime.datetime.now()

print(now)
print(now.strftime('%d.%m.%Y'))
print(now.strftime('%d %B %y  %A'))
print(now.strftime('%H:%M'))

date_str = '2023-02-17 12:50:16.291779'
d = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
print(d)
print([d])
