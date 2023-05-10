from concurrent.futures import ThreadPoolExecutor
import time
from random import randint


def task(number: int) -> str:
    print(f"worker executing task number {number}")
    sleep_period = randint(0, 3)
    time.sleep(sleep_period)
    return str(number + sleep_period)


def task2(number: int) -> str:
    print(f"another call: worker executing task number {number}")
    sleep_period = randint(0, 3)
    time.sleep(sleep_period)
    return str(number + sleep_period)


def task3(number: int) -> str:
    print(f"using map: worker executing task number {number}")
    sleep_period = randint(0, 3)
    time.sleep(sleep_period)
    return str(number + sleep_period)


def start_threads():
    executor = ThreadPoolExecutor(max_workers=3)

    [executor.submit(task, x) for x in range(10)]
    executor.shutdown(wait=False)


def start_threads_anothertime():
    executor = ThreadPoolExecutor(max_workers=3)

    [executor.submit(task2, x) for x in range(10)]
    executor.shutdown(wait=False)


if __name__ == "__main__":
    start_threads()
    # default context manager behavior:
    # ex.shutdown(wait=True, cancel_futures=False)
    #
    # this means that the context manager will wait for all futures to complete
    #
    print("main has resumed again after dispatching tasks")

    print("dispatching similar tasks for the second time")
    with ThreadPoolExecutor(4) as exe:
        _ = exe.map(task2, range(10))
    print("more tasks")
    start_threads_anothertime()

    print("FIN")
