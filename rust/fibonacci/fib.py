import rust
from timeit import default_timer as timer


inputs = [
    {"number": 150},
]


def get_fibonacci(n):
    n -= 1
    fib_seq = [0]
    while n > 0:
        n -= 1
        if len(fib_seq) == 1:
            fib_seq.append(1)
        else:
            last = fib_seq[-1]
            second_to_last = fib_seq[-2]
            fib_seq.append(last + second_to_last)

    return fib_seq[-1]


def python_fib():
    start = timer()
    for _ in range(10000):
        get_fibonacci(150)

    elapsed = timer() - start

    print("Python completed in {:.2f} seconds.".format(elapsed))


def rust_fib():
    start = timer()
    for _ in range(10000):
        rust.get_fibonacci(150)
    elapsed = timer() - start
    print("Rust completed in {:.2f} seconds.".format(elapsed))


def run_once():

    start = timer()
    print(rust.get_fibonacci_big(2000))
    elapsed = timer() - start

    print("Rust with completed in {:.2f} seconds.".format(elapsed))

    start = timer()
    print(getNthFib(1000))
    elapsed = timer() - start

    print("Python completed in {:.2f} seconds.".format(elapsed))


if __name__ == "__main__":

    python_fib()
    rust_fib()

    # run_once()
