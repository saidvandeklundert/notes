"""
Run as main to consume the API.


"""
from pydoc import resolve
import requests
from pprint import pprint


def read_all_customers():
    api_url = "http://127.0.0.1:8000/customers"
    response = requests.get(api_url)
    pprint(response.json())


if __name__ == "__main__":
    read_all_customers()
