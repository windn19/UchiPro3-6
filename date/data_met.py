import datetime


d = datetime.datetime.today()

print(d)
print(d.isocalendar())
print(d.isoformat())
print(d.isoweekday())
print(d.strftime('%d-%m-%Y'))
print(d.replace(month=4))
