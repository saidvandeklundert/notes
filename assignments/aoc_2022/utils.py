import functools
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def timer(func):
    """Log the time it takes to a function"""

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        logger.info(f"starting run of '{func.__name__}'")
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"'{func.__name__}' completed in {end_time - start_time:.2f}")
        return value

    return wrapped
