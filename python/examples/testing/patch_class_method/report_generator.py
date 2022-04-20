"""

A class that is used in test_mock_function_return.py

"""
import time


class ReportGenerator:
    def generate_report(self):
        numbers = self._get_information_from_database()
        return sum(numbers)

    def _get_information_from_database(self):
        """Retrieve a list of values from a database"""
        time.sleep(5)
        return [10, 10]
