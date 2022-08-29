import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize


def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


def slow() -> int:
    time.sleep(3)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=("thinking!", done))  # start another process
    print(f"spinner object: {spinner}")
    spinner.start()  # start spinning
    result = slow()  # run the slow function
    done.set()  # end the process
    spinner.join()  # wait for the process to finish
    return result


def main() -> None:
    result = supervisor()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
