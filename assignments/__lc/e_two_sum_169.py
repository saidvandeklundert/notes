from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums):
            for idx, number_2 in enumerate(nums):
                if idx != index:
                    if number + number_2 == target:
                        return [index, idx]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index, number in enumerate(nums):
            mapping[number] = index

        for index, number in enumerate(nums):
            lookup_value = target - number
            if mapping.get(lookup_value):
                if index != mapping[lookup_value]:
                    return [index, mapping[lookup_value]]


class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        for idx in range(len(arr)):  # O(n)
            new_target = target - arr[idx]
            lft, rght = idx + 1, len(arr) - 1
            while lft <= rght:  # O(logn)
                mid = lft + (rght - lft) // 2
                if arr[mid] == new_target:
                    return [idx + 1, mid + 1]
                elif arr[mid] > new_target:
                    rght = mid - 1
                else:
                    lft = mid + 1
