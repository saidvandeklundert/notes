"""
Returns the index of the target if present, -1 in case the target is not present.
"""
from typing import List, Optional


def binary_search(
    arr: List[int], target: int, low: int = 0, high: Optional[int] = None
):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1

    middle = (low + high) // 2
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search(arr, target, low, middle - 1)
    else:
        return binary_search(arr, target, middle + 1, high)


tests = [
    ([0, 2, 14, 144, 43256, 2342366, 123124], 43256),  # 4
    ([0, 2, 14, 144, 43256, 2342366, 123124], 1),  # -1
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8),  # 8
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3),  # 3
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4),  # 4
]

for x in tests:
    print(binary_search(x[0], x[1]))
