import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait


def task(number: int):
    time.sleep(1)
    return f"All Done with task {number}"


if __name__ == "__main__":
    with ThreadPoolExecutor() as ex:
        futures = [ex.submit(task, i) for i in range(10)]

        for future in as_completed(futures):
            result = future.result()

            print(result)

    with ThreadPoolExecutor() as ex:
        futures = [ex.submit(task, i) for i in range(10)]

    for future in futures:
        result = future.result()

        print(result)
