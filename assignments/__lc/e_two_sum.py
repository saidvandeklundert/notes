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
