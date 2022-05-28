"""
Returns the index of the target if present, -1 in case the target is not present.

Finds the leftmost result.
"""
from typing import List
import bisect


def binary_search(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            result = middle
            low = middle + 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return result


tests = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 88, 9], 8),  # 8
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3),  # 3
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4),  # 4
    ([0, 1, 2, 3, 4, 4, 4, 4], 4),  # 4
]

for x in tests:
    print(binary_search(x[0], x[1]))
    # bisect_right returns an insertion point which comes after, hence the +1 diff
    print(bisect.bisect_right(x[0], x[1]))
