from requests.api import get
import backoff
import requests

URLS = [
    "http://nu.nl",
    "http://nos.nl",
    "http://ffqwerqwrqwr.nl",
]


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException)
def get_url(url):
    return requests.get(url)


if __name__ == "__main__":
    for url in URLS:
        print(get_url(url=url))