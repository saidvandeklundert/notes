from concurrent.futures import ProcessPoolExecutor
import time


def task():
    print("running a task", flush=True)
    time.sleep(1)
    print("task completed", flush=True)


if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        # start the task:
        future = ex.submit(task)

        # eait for the task to complete:
        future.result()
