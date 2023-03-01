import datetime

date = datetime.datetime.strptime(input(), '%d.%m.%Y')

year = date.year
while year == date.year:
   if date.isoweekday() > 5:
       print(date.strftime('%d.%m.%Y'))
   date += datetime.timedelta(days=1)