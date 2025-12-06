from mylib import throttle
import time

@throttle.throttle(10)
def hello():
    print("Hello!")

hello()
hello()
time.sleep(10.1)
hello()