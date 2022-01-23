import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    print(f"Starting to count to {count_to}.")
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f"Finished couting to {count_to} in {end - start}.")
    return counter


if __name__ == "__main__":
    with ProcessPoolExecutor() as process_pool:
        numbers = [
            200000000,
            1,
            2,
            3,
            200000001,
            4,
            5,
            200000002,
            200000003,
            6,
            7,
            8,
            9,
            10000,
            10000000,
        ]
        for result in process_pool.map(count, numbers):
            print(result)