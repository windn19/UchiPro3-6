import datetime

day = datetime.date.today()
t = datetime.datetime.now().time()
print(day, t, sep='\n')

d = datetime.datetime.combine(day, t)
print(d)
print([d])


