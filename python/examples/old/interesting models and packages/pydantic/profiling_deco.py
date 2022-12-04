import cProfile
from functools import wraps
from pstats import Stats, SortKey
from time import time


def time_func(f):
    """Timing a function"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f"Elapsed time {f.__name__}: {end - start}")
        return result

    return wrapper


def profile_func(f):
    """Profiling a function"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        with cProfile.Profile() as pr:
            result = f(*args, **kwargs)
        ps = Stats(pr)
        print("Most time spent in:")
        ps.sort_stats(SortKey.CUMULATIVE).print_stats(10)
        print("Functions taking most CPU time:")
        ps.sort_stats(SortKey.TIME).print_stats(10)
        return result

    return wrapper