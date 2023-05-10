import time
from concurrent.futures import ProcessPoolExecutor, wait


def task(number: int):
    time.sleep(1)
    return f"All Done with task {number}"


if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        futures = [ex.submit(task, i) for i in range(10)]

        done_futures, _ = wait(futures)

    while len(done_futures) > 0:
        future = done_futures.pop()
        if future is None:
            break
        result = future.result()
        print(result)
