from random import random
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def task(number):
    value = random()
    print(f"Task generated {value}")
    sleep(value)
    return number + value


if __name__ == "__main__":
    with ThreadPoolExecutor() as ex:
        futures = [ex.submit(task, i) for i in range(5)]

    print("WORK IS DONE, CHECKING RESULTS\n\n\n\n")
    for future in futures:
        print(future.result())
