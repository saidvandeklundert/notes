import urllib.request


def url_ok(url: str):
    return urllib.request.urlopen(url).getcode()
