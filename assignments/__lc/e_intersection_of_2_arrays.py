from typing import List, Tuple, Optional


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1_nr in nums1:
            ans, pos = self.search(num1_nr, nums2)
            print(ans, pos)
            if ans:
                # del to remove the item, speeding up subsequent searches
                del nums2[pos]
                # adding the answer to the list
                res.append(num1_nr)
        return res

    def search(self, value: int, nums: List[int]) -> Tuple[Optional[bool], int]:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            m = left + (right - left) // 2
            if nums[m] == value:
                return True, m
            elif nums[m] < value:
                left = m + 1
            else:
                right = m - 1
        return None, -1


alist = [
    ([1, 2, 2, 1], [2, 2]),  # [2,2]
    ([4, 9, 5], [9, 4, 9, 8, 4]),  # [4,9]
]

for x in alist:
    print(Solution().intersect(x[0], x[1]))
