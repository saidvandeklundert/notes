from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from random import randint


def task(number: int) -> str:
    print(f"worker executing task number {number}")
    sleep_period = randint(0, 6)
    if sleep_period > 3:
        raise RuntimeError("sleep period too long")
    time.sleep(sleep_period)
    return str(number + sleep_period)


if __name__ == "__main__":
    """"""
    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_url = {executor.submit(task, nr): nr for nr in range(20)}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f"{exc}")
            else:
                print(f"{data}")
