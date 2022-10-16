import time
import random


def get_database_data():
    time.sleep(5)
    return [random.randint(0, 100000000000) for x in range(10)]


def get_report():
    """Function that takes interface counters and calculates
    the average traffic."""

    # getting items from database:
    data = get_database_data()

    # complex calculations
    average = sum(data) // len(data)
    return average


class ReportGenerator:
    """
    Class that generates traffic reports.
    """

    def generate_report(self):
        # getting the data from the database:
        data = self._get_database_data()
        # complex calculations
        average = sum(data) // len(data)
        return average

    @staticmethod
    def _get_database_data():
        time.sleep(5)
        return [random.randint(0, 100000000000) for x in range(10)]
