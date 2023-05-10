from time import sleep
from concurrent.futures import ThreadPoolExecutor
from threading import active_count


def task(number):
    sleep(1)
    print(f"Active workers: {active_count()}, executing task {number}")


def init():
    print("Initializing worker...")


if __name__ == "__main__":
    with ThreadPoolExecutor(50, initializer=init) as exe:
        _ = exe.map(task, range(200))
