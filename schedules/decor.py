import time

from schedule import every, repeat, run_pending


@repeat(every(2).seconds, "World")
@repeat(every(4).seconds, "Mars")
def hello(planet):
    print("Hello", planet)


while True:
    run_pending()
    time.sleep(1)