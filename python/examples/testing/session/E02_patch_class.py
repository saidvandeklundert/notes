import time
import random


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
        return [random.randint(0, 100000000000) for _ in range(10)]
