import datetime

weekdays = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

date = datetime.datetime.strptime(input(), '%m %Y')
month = date.month
print(*weekdays, sep='\t', end='\t')
print()
print('\t' * date.weekday(), end='')
while month == date.month:
   print(date.day, end='\t')
   if date.isoweekday() == 7:
       print()
   date += datetime.timedelta(days=1)
print()
