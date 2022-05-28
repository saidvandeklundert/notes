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
            high = middle - 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return result


tests = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 88, 9], 8),  # 8
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3),  # 3
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4),  # 4
]

for x in tests:
    print(binary_search(x[0], x[1]))
    print(bisect.bisect_left(x[0], x[1]))


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for e in nums1:
            ans, pos = self.search(e, nums2)
            if ans:
                del nums2[pos]  # will make BS more quick
                res.append(e)
        return res

    def search(self, value, a):
        a.sort()
        l, r = 0, len(a) - 1
        while l <= r:
            m = l + (r - l) // 2
            if a[m] == value:
                return True, m
            elif a[m] < value:
                l = m + 1
            else:
                r = m - 1
        return None, -1
