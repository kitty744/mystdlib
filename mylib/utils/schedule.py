import time as _time
import threading as _threading

def after(seconds, func, *args, **kwargs):
    def wrapper():
        _time.sleep(seconds)
        func(*args, **kwargs)

    _threading.Thread(target=wrapper).start()

def every(seconds, func, *args, **kwargs):
    def wrapper():
        while True:
            func(*args, **kwargs)

            _time.sleep(seconds)

    _threading.Thread(target=wrapper).start()