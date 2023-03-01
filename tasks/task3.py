import datetime

total = 0
max_count = 3
count = int(input())
date = datetime.datetime.strptime(input(), '%d.%m.%Y')

while total < 4:
   if count < max_count:
       if date.isoweekday() in [6, 7] and date.day % 2 == 0:
           print(date.strftime('%d.%m.%Y'))
           total += 1
           count += 1
       date += datetime.timedelta(days=1)
   else:
       date = date + datetime.timedelta(days=30)
       count = 0