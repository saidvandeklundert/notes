from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for x in nums:
            if seen.get(x) is None:
                seen[x] = 1
            else:
                seen[x] += 1
        for k, v in seen.items():
            if v == 1:
                return k
            else:
                pass


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = collections.Counter(nums)
        for k, v in seen.items():
            if v == 1:
                return k


if __name__ == "__main__":
    lists = [[2, 2, 1], [4, 1, 2, 1, 2]]
    for alist in lists:
        print(Solution().singleNumber(alist))
