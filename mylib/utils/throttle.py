import time
import functools
from typing import Callable

def throttle(interval: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            last = getattr(wrapper, "_last_call", None)

            if last is None or (now - last) >= interval:
                setattr(wrapper, "_last_call", now)
                return func(*args, **kwargs)

            return None  # throttled, too soon

        wrapper._last_call = None
        return wrapper

    return decorator
