import datetime


s = '2023/01/31'

date = datetime.datetime.strptime(s, '%Y/%m/%d')
print(date.strftime('%d.%m.%Y'))
