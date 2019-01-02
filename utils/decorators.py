from functools import wraps
from datetime import datetime


def time_it(func):
    """
    Time it helper annotation
    :param func: function that is being timed
    :return: time in Hours.Minutes.Seconds.Milliseconds format
    """

    @wraps(func)
    def wrapped(*args, **kwargs):
        start_time = datetime.now()
        ret = func(*args, **kwargs)
        end_time = datetime.now() - start_time
        print("Function: {} took {} to evaluate.".format(func.__name__, end_time))
        return ret

    return wrapped
