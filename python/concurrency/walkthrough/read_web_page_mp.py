from concurrent.futures import ProcessPoolExecutor
from concurrent import futures
from multiprocessing import cpu_count
import requests
from typing import Union
from datetime import datetime


def read_urls() -> list[str]:
    """Read URLs form a file and return them
    as a list."""
    with open("url_list.txt", "r") as f:
        urls = f.readlines()
    urls = [url.strip() for url in urls]
    return urls


def get_page(url: str) -> Union[requests.Response, Exception]:
    """Return the page for target website."""
    try:
        response = requests.get(url, timeout=4)
    except Exception as err:
        return err
    return response


def main():
    fut: list[futures.Future] = []
    urls = read_urls()
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        for url in urls:
            fut.append(executor.submit(get_page, url))

    print("All threads are done.")

    # focus on the requests that succeeded:
    for future in fut:
        resp = future.result()
        if isinstance(resp, requests.Response):
            print(
                f"{resp.url} returned code {resp.status_code}",
                f"first characters: {resp.text[0:10]}",
            )
    # deal with the failures:
    for future in fut:
        resp = future.result()
        if not isinstance(resp, requests.Response):
            print(
                f"ERROR {resp}",
            )


if __name__ == "__main__":

    startTime = datetime.now()
    main()
    duration = datetime.now() - startTime
    print(f"script took {duration}")
    # script took 0:00:14.111311
