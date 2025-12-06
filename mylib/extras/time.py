import time as _time
from datetime import datetime, timezone

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def sleep(seconds):
    _time.sleep(seconds)

def timestamp():
    return int(_time.time())

def today():
    return datetime.today().strftime("%Y-%m-%d")

def utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")