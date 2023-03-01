import datetime
import time
import os

import schedule


def print_time():
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S'))


schedule.every().seconds.do(print_time)
while 1:
    schedule.run_pending()
    time.sleep(1)
    os.system('clear')
