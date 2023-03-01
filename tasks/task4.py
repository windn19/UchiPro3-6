import datetime
import time

import schedule


def print_time():
    now_date = datetime.datetime.now()
    new_year = datetime.datetime(now_date.year, 12, 31)
    delta = new_year - now_date
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    print(f'До нового года осталось дней: {days}, часов: {hours}, минут: {minutes}, секунд: {seconds}.')


schedule.every().seconds.do(print_time)

while True:
    schedule.run_pending()
    time.sleep(1)
