import functools
from datetime import datetime, timedelta


def cache_with_expiry(duration):
    def decorator(func):
        @functools.lru_cache(maxsize=None)
        def wrapper(*args, **kwargs):
            current_time = datetime.now()
            expiry_time = current_time + timedelta(hours=duration)
            return func(*args, **kwargs)

        return wrapper

    return decorator
