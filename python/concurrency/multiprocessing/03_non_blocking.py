from concurrent.futures import ProcessPoolExecutor
import time


def sleep() -> None:
    time.sleep(4)
    print("Done sleeping")


if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        _ = ex.map(sleep, range(10))
    print("not blocked!")

    time.sleep(10)
    print("fin")
    # the processes complete on their own
