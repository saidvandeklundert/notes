import contextlib
import signal
from types import FrameType
from typing import Generator
import time
from sys import argv


class Timeout(Exception):
    pass


def alarm_handler(signum: int, frame: FrameType) -> None:
    print("Signal handler called with signal", signum)
    raise Timeout()


@contextlib.contextmanager
def timeout(s: int) -> Generator[None, None, None]:
    original_signal = signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(s)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, original_signal)


def main(wait: int) -> int:
    with timeout(2):
        print("timing out")
        time.sleep(wait)
    time.sleep(5)
    return 0


if __name__ == "__main__":
    if len(argv) == 2:
        wait = int(argv[1])
        print(wait)
        raise SystemExit(main(wait))
    else:
        print("Pass a timeout value")