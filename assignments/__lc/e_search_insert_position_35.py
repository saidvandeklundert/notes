"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 

If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num == target:
                return index
            elif num > target and index in [0, 1]:
                return index
            elif num > target:
                return index
        else:
            return len(nums)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    ret = Solution().searchInsert([2, 3, 5, 6], 2)
    print(ret)
    ret = Solution().searchInsert([1, 3, 5], 4)
    print(ret)
    ret = Solution().searchInsert([1, 3, 5, 6], 7)
    print(ret)
    ret = Solution().searchInsert([1, 3, 5, 6], 0)
    print(ret)
