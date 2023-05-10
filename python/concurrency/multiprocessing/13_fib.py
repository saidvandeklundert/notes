import time
from concurrent.futures import ProcessPoolExecutor


def fib(n: int) -> int:
    n0, n1 = 0, 1

    for _ in range(0, n):
        n0, n1 = n1, (n1 + n0)
    return n0


if __name__ == "__main__":
    start_time = time.time()
    numbers = range(10000)

    fibs = map(fib, numbers)

    results = dict(zip(numbers, fibs))
    elapsed_time = time.time() - start_time
    print(f"non parallel execution done in {elapsed_time}")

    start_time = time.time()
    with ProcessPoolExecutor() as ex:
        results = ex.map(
            fib,
            numbers,
        )

    elapsed_time = time.time() - start_time
    print(f"parallel execution done in {elapsed_time}")

    start_time = time.time()
    with ProcessPoolExecutor() as ex:
        results = ex.map(fib, numbers, chunksize=50)

    elapsed_time = time.time() - start_time
    print(f"parallel execution in chunks done in {elapsed_time}")
