import datetime


date = datetime.datetime(2023, 3, 1)
month = date.month
while date.month == month:
    if date.isoweekday() in [6, 7]:
        print(f'{date.strftime("%d.%m")} - выходной!')
    date += datetime.timedelta(days=1)
