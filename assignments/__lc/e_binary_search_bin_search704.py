from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        middle = end // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            middle = middle + 1
            return helper(nums=nums, target=target, start=middle, stop=end)
        elif nums[middle] > target:
            middle = middle - 1
            return helper(nums=nums, target=target, start=0, stop=middle)


def helper(nums: List[int], target: int, start: int, stop: int) -> int:

    middle = (stop - start) // 2 + start
    print("start", start, "stop", stop, "middle", middle)
    if nums[middle] == target:
        print("MIDDLE")
        return middle
    elif start - stop == 1:
        return -1
    elif nums[middle] < target:
        middle = middle + 1
        return helper(nums=nums, target=target, start=middle, stop=stop)
    elif nums[middle] > target:
        middle = middle - 1
        return helper(nums=nums, target=target, start=start, stop=middle)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1


alist = [
    [[-1, 0, 3, 5, 9, 12], 9],  # 4
    [[-1, 0, 3, 5, 9, 12], 2],  # -1
]

for x in alist:
    print(Solution().search(x[0], x[1]))
for x in alist:
    print(search(x[0], x[1]))
