import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:
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
    spinner = Thread(target=spin, args=("thinking!", done))
    print(f"spinner object: {spinner}")
    spinner.start()  # start the thread
    result = slow()  # perform a task while the spinner keeps running
    done.set()  # set the event flag to true
    spinner.join()  # wait for the spinner thread to finish
    return result


def main() -> None:
    result = supervisor()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
