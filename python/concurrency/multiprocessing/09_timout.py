import time
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import TimeoutError


def task():
    time.sleep(1)
    return "All Done"


if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        future = ex.submit(task)

        try:
            result = future.result(timeout=0.5)

            print(f"Got Result: {result}")
        except TimeoutError:
            print("Gave up waiting for a result")
        try:
            for result in ex.map(task, timeout=0.4):
                print(result)
        except TimeoutError:
            print("Gave up waiting for a result")
