from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for number in nums:
            if seen.get(number):
                return True
            seen[number] = True
        return False


alist = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

for nums in alist:
    print(Solution().containsDuplicate(nums))
