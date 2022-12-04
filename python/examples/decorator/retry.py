from functools import wraps
import logging
import random

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class ControlledException(Exception):
    """Specific Exception type we want to have trigger a
    retry."""


def retry(operation):
    """
    The decorator that takes in a function
    and ensures that it will be tried a few times.

    The retry will only happen in case a
    'ControlledException' is raised by the function that was passed in.
    """

    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised: None | ControlledException = None
        RETRIES_LIMIT = 30
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                logger.info("retrying %s", operation.__qualname__)
                last_raised = e
        raise last_raised

    return wrapped


@retry
def run_task():
    num = random.randint(1, 15)
    if num < 3:

        return num
    else:
        raise ControlledException(f"{num} has unacceptable value")


if __name__ == "__main__":
    print(run_task())
