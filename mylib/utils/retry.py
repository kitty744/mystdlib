import time
import functools
import random

def retry_call(
    func,
    *args,
    attempts=3,
    delay=1,
    exceptions=(Exception,),
    backoff=1,
    jitter=0,
    on_retry=None,
    **kwargs
):

    last_exc = None

    for attempt in range(1, attempts + 1):
        try:
            return func(*args, **kwargs)
        except exceptions as e:
            last_exc = e

            if attempt == attempts:
                raise

            sleep_time = delay * (backoff ** (attempt - 1))

            if jitter:
                sleep_time += random.uniform(0, jitter)

            if on_retry:
                try:
                    on_retry(attempt, e, sleep_time)
                except Exception:
                    pass

            time.sleep(sleep_time)

    if last_exc:
        raise last_exc


def _retry_factory(
    attempts=3,
    delay=1,
    backoff=1,
    jitter=0,
    exceptions=(Exception,),
    on_retry=None,
):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return retry_call(
                func,
                *args,
                attempts=attempts,
                delay=delay,
                backoff=backoff,
                jitter=jitter,
                exceptions=exceptions,
                on_retry=on_retry,
                **kwargs
            )
        return wrapper
    return decorator


def retry(*d_args, **d_kwargs):
    """
    The public decorator.

    Works with:
    @retry
    or
    @retry(attempts=3, delay=1)
    """
    # Case: @retry without parentheses
    if d_args and callable(d_args[0]):
        return _retry_factory()(d_args[0])

    # Case: @retry(...)
    return _retry_factory(**d_kwargs)
