from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        print(nums)

        idx = 0
        last = len(nums) - 1
        pointer_to_ = last
        while idx <= last:
            if nums[idx] == val:
                nums[idx] = "_"
                nums[idx], nums[pointer_to_] = nums[pointer_to_], nums[idx]
                pointer_to_ -= 1
            else:
                idx += 1

        return pointer_to_ + 1


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == "__main__":
    l = [([3, 2, 2, 3], 3), ([2], 3)]
    for t in l:
        print(Solution().removeElement(t[0], t[1]))
