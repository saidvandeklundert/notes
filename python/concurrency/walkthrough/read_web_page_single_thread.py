import requests
from datetime import datetime
from typing import Union


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
    for url in read_urls():

        resp = get_page(url)
        if isinstance(resp, requests.Response):
            print(
                f"{url} returned code {resp.status_code}",
                f"first characters: {resp.text[0:10]}",
            )
        else:
            print(resp)


if __name__ == "__main__":

    startTime = datetime.now()
    main()
    duration = datetime.now() - startTime
    print(f"script took {duration}")
    # script took 0:01:48.189630
