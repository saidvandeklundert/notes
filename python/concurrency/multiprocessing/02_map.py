from concurrent.futures import ProcessPoolExecutor

# map runs a function for every item in an iterable


def double(x: int) -> int:
    return x * 2


alist = [1, 2, 3]

for result in map(double, alist):
    print(result)

    # ProcessPoolExecutor also has a map method:


def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        for result in ex.map(double, alist):
            print(result)

    with ProcessPoolExecutor() as ex:
        for result in ex.map(multiply, alist, range(len(alist))):
            print(result)
