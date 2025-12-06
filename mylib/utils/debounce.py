import threading
import functools
from typing import Callable

def debounce(delay: float):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timer = getattr(wrapper, "_timer", None)

            if timer is not None:
                timer.cancel()
            
            t = threading.Timer(delay, lambda: func(*args, **kwargs))
            t.start()
            wrapper._timer = t
        
        wrapper._timer = None
        return wrapper
    return decorator