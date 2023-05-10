from concurrent.futures import ThreadPoolExecutor
import time
from random import randint


def task(number: int) -> str:
    print(f"worker executing task number {number}")
    sleep_period = randint(0, 6)
    time.sleep(sleep_period)
    return str(number + sleep_period)


if __name__ == "__main__":
    with ThreadPoolExecutor(50) as ex:
        for result in ex.map(task, range(100)):
            print(result)
    # default context manager behavior:
    # ex.shutdown(wait=True, cancel_futures=False)
    #
    # this means that the context manager will wait for all futures to complete
