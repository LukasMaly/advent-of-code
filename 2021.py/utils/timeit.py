from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kw):
        start_time = time.perf_counter()
        try:
            return func(*args, **kw)
        finally:
            end_time = time.perf_counter()
            print(f"{func.__name__!r} took {(end_time - start_time) * 1000:.3f} ms")
    return wrapper
