import rust
from timeit import default_timer as timer


inputs = [
    {"number": 150},
]


def python_fib():
    start = timer()
    for number in range(150):
        getNthFib(number)
    print(getNthFib(number))

    elapsed = timer() - start

    print("Python completed in {:.2f} seconds.".format(elapsed))


def rust_fib():
    start = timer()
    for number in range(150):
        rust.get_fibonacci(number)
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
