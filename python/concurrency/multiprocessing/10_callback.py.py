from time import sleep
from concurrent.futures import ProcessPoolExecutor


def callback(future):
    print("The custom callback was called.")
    result = future.result()
    print(result)


def task() -> int:
    sleep(1)
    print("The task is done.")
    return 100


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        future = executor.submit(task)

        future.add_done_callback(callback)
