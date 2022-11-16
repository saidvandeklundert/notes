import requests
from requests.exceptions import Timeout
from typing import Union


def api_call() -> Union[str, None]:
    try:
        r = requests.get("http://localhost/api/does_not_even_exist")
        if r.status_code == 200:
            return r.json()
    except Timeout as err:
        print("Handle timeout logic")
        raise err


def api_call_paginated():
    req = requests.get("http://localhost/api/does_not_even_exist")
    data = req.json()
    while data.get("next_token") is not None:

        next_token = data.get("next_token")
        req = requests.get(
            f"http://localhost/api/does_not_even_exist?page={next_token}"
        )
        additional_data = req.json()
        print(additional_data)
        data.update(additional_data)
    return data
