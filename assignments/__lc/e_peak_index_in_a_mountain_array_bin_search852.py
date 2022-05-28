from typing import List


class Solution:
    """Linear scan"""

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak_value = 0
        peak_index = 0
        for index, x in enumerate(arr):
            if x > peak_value:
                peak_value = x
                peak_index = index
        return peak_index


class Solution(object):
    """Binary search"""

    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo


alist = [
    [0, 1, 0],  # 1
    [0, 2, 1, 0],  # 1
    [0, 10, 5, 2],  # 1
]
