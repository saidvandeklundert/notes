from platform import mac_ver
from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    most_wealth = 0
    for person in accounts:
        potential = 0
        for acc in person:
            potential += acc

        if potential > most_wealth:
            most_wealth = potential

    return most_wealth


print(maximumWealth([[1, 5], [7, 3], [3, 5]]))
