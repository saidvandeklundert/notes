from concurrent.futures import ThreadPoolExecutor
import time
from os import getpid

THREAD_COUNT = 20


def io_bound_function(parameter) -> None:
    """
    Simulates an IO-bound function using time.sleep(3).
    """
    print(f"io_bound_function called with argument {parameter} using PID {getpid()}")
    time.sleep(3)
    print(f"io_bound_function with argument {parameter} using PID {getpid()} ended")


def example_process_pool():
    with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
        for id in range(THREAD_COUNT):
            executor.submit(io_bound_function, id)


if __name__ == "__main__":
    example_process_pool()
