import rust
from timeit import default_timer as timer

"""
    {"number": 1},
    {"number": 2},
    {"number": 3},
    {"number": 4},
    {"number": 5},
    {"number": 6},
    {"number": 7},
    {"number": 8},
    {"number": 9},
    {"number": 10},
    {"number": 11},
    {"number": 12},
    {"number": 13},
    {"number": 14},
    {"number": 15},
    {"number": 16},
    {"number": 17},
    {"number": 18},
    {"number": 19},
    {"number": 20},
    {"number": 25},
    {"number": 30},
    {"number": 35},
    {"number": 40},
    {"number": 45},
    {"number": 50},    
    {"number": 100},
"""

inputs = [
    {"number": 175},
]


def getNthFib(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2

    fib_seq = [0]
    while number > 0:
        number -= 1
        if len(fib_seq) == 1:
            fib_seq.append(1)
        else:
            last = fib_seq[-1]
            second_to_last = fib_seq[-2]
            fib_seq.append(last + second_to_last)

    return fib_seq[-1]


def getNthFib_a(number):
    fib_seq = [0, 1]
    counter = 3
    while counter <= number:
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq[0] = fib_seq[1]
        fib_seq[1] = next_fib
        counter += 1

    return fib_seq[1] if number > 1 else fib_seq[0]


def getNthFib_rec(number):
    if number == 2:
        return 1
    elif number == 1:
        return 0
    else:
        return getNthFib_rec(number - 1) + getNthFib_rec(number - 2)


def python_fib(number):
    start = timer()
    for _ in range(10000):
        result = getNthFib(number)
    elapsed = timer() - start
    # print(f"Python got {result} in {elapsed}.")
    print(f"Python  in {elapsed}.")


def rust_fib(number):
    start = timer()
    for _ in range(10000):
        result = rust.get_fibonacci(number)
    elapsed = timer() - start
    # print(f"Rust got {result} in {elapsed}.")
    print(f"Rust in {elapsed}.")


if __name__ == "__main__":
    for test in inputs:
        python_fib(**test)
        rust_fib(**test)
        print(50 * "-")
