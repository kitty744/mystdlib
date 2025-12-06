import time as _time

_start_time = None
_end_time = None

def start():
    global _start_time
    _start_time = _time.time()

def stop():
    global _end_time
    _end_time = _time.time()

def elapsed():
    if _start_time is None:
        return 0  # timer hasn't started
    if _end_time is None:
        return _time.time() - _start_time  # timer running
    return _end_time - _start_time  # timer stopped