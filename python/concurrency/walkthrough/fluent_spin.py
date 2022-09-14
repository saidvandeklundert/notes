import itertools
import time


def spin(
    msg: str,
) -> None:
    for char in itertools.cycle(r"\|/-"):
        time.sleep(0.1)
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)

    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


if __name__ == "__main__":
    spin("thinking")
    print("fin")
