from functools import lru_cache


def fib_no_cache(n):
    if n < 2:
        return n
    return fib_no_cache(n - 2) + fib_no_cache(n - 1)


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    print("starting fib_no_cache")
    print(fib_no_cache(35))
    print("done with fib_no_cache")
    print("starting larger fib calculation WITH caching:")
    print(fib.cache_info())
    print(fib(50))
    print(fib.cache_info())
    print(fib(55))
    print(fib.cache_info())
    print(fib(60))
    print(fib.cache_info())
    print(fib(80))
    print(fib.cache_info())
