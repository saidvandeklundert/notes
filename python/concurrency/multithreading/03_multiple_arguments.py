from concurrent.futures import ThreadPoolExecutor


def task(*args, **kwargs) -> str:
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)
    return "done"


if __name__ == "__main__":
    with ThreadPoolExecutor() as ex:
        future = ex.submit(task, 11, 12, 13, d=2)

        result = future.result
        print(result())

    alist = [
        (1, 2, 3, {"a": 1}),
        (1, 2, 3, {"b": 1}),
        (1, 2, 3, {"c": 1}),
    ]
    with ThreadPoolExecutor() as ex:
        for result in ex.map(task, *alist):
            result = future.result
            print(result())
