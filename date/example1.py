import datetime

weekdays = ['понедельник', "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

today = datetime.date.today()
weekday = today.weekday()

print(f'Сегодня: {weekdays[weekday]}')
