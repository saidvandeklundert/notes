from functools import wraps
import time
import random


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


MAX = 1_000_000
STRING = "\n".join([f"some random line of text {x}" for x in range(MAX)])
SET = set(STRING.splitlines())


@timeit
def using_string():
    x = random.randint(0, MAX)
    for _ in range(10_000):
        assert str(f"some random line of text {x}") in STRING


@timeit
def using_set():
    x = random.randint(0, MAX)
    for _ in range(10_000):
        assert str(f"some random line of text {x}") in SET


if __name__ == "__main__":
    print(using_string())
    print(using_set())
