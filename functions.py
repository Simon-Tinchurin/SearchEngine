from functools import wraps
import datetime

functions_work_time = {}


def timer(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.datetime.now()
            delta = (end_time - start_time).total_seconds()
            functions_work_time[func.__name__] = delta
            print(func.__name__, delta)
            return result
        return wrapper
    return decorator(func)