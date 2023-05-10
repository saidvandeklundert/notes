from concurrent.futures import ProcessPoolExecutor


def task(number: int) -> int:
    return number * 2


if __name__ == "__main__":
    with ProcessPoolExecutor(4) as exe:
        _ = exe.map(task, range(10000))

    print("All done, no chunks")
    with ProcessPoolExecutor(4) as exe:
        _ = exe.map(task, range(10000), chunksize=500)

    print("All done")
