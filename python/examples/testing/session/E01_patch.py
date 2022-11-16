import time
import random


def get_database_data():
    time.sleep(5)
    return [random.randint(0, 100000000000) for x in range(10)]


def get_report():
    """Function that takes interface counters and calculates
    the average traffic."""

    # get the counters from a database:
    data = get_database_data()

    # perform complex calculations:
    average = sum(data) // len(data)
    return average
