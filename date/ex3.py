import datetime
import time


now_minute = datetime.datetime.now().minute
while True:
    now = datetime.datetime.now()
    if now.minute != now_minute:
        print('\n', now.strftime('%H:%M'))
        now_minute = now.minute
    print(now.second, end='->')
    time.sleep(1)
