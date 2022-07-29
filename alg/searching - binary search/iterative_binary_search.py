"""
Returns the index of the target if present, -1 in case the target is not present.
"""
from typing import List


def binary_search(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1


tests = [
    ([0, 2, 14, 144, 43256, 2342366, 123124], 43256),  # 4
    ([0, 2, 14, 144, 43256, 2342366, 123124], 1),  # -1
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8),  # 8
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3),  # 3
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4),  # 4
    ([5], 5),  # 0
    ([-1, 0, 3, 5, 9, 12], 2),  # -1
]

for x in tests:
    print(binary_search(x[0], x[1]))
