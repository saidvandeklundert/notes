import requests
import time
import random


def get_item_from_database():
    time.sleep(5)
    return str(random.randint(0, 100))


class ReportGenerator:
    def generate_report(self):
        numbers = self._get_information_from_database()
        return sum(numbers)

    def _get_information_from_database(self):
        """Retrieve a list of values from a database"""
        time.sleep(5)
        return [10, 10]


def sunny(location: str) -> bool:
    url = f"https://weatherdbi.herokuapp.com/data/weather/{location}"
    api_response_str = requests.get(url)
    api_response_d = api_response_str.json()
    if "sunny" in api_response_d["currentConditions"]["comment"].lower():
        return True
    else:
        return False
