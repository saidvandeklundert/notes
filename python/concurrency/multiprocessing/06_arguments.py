from concurrent.futures import ProcessPoolExecutor


def task(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)


if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        future = ex.submit(task, 11, 12, 13, d=2)

        result = future.result
        print(result)

    alist = [
        (1, 2, 3, {"a": 1}),
        (1, 2, 3, {"b": 1}),
        (1, 2, 3, {"c": 1}),
    ]
    with ProcessPoolExecutor() as ex:
        for result in ex.map(task, *alist):
            result = future.result
            print(result)
