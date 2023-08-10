"""
The general idea of a decorator is that it creates a
 function that returns another function.

In a sense, this makes it a a higher-order function.

In the first example, the internal function defined in the the decorator is going to be the one being called.
"""
import functools
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def timer(func):
    """Log the time it takes to run the function"""

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        """
        Function that 'wraps around' the decorated function.

        In essence, the decorated function will be run by this function.
        """
        logger.info(f"'wrapped' is going to run '{func.__name__}'")
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"completed '{func.__name__}' in {end_time - start_time:.2f} secs")
        return value

    return wrapped


@timer
def some_task(num_times):
    for num in range(num_times):
        sum([i**2 for i in range(10000)])
        print(num)


@timer
def some_other_task(num_times):
    for num in range(num_times):
        sum([i**2 for i in range(10000)])
        print(num)


some_task(2)
some_other_task(3)

some_task(2)


try:
    0 / 0
except Exception as e:
    print(e)
    print(str(e))
