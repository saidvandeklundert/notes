# Time: on average O(nlgn), worst case O(n^2)
# Space: O(n)


def sortArray(nums: list[int]) -> list[int]:
    if not nums:
        return nums
    quickSort(0, len(nums) - 1, nums)
    return nums


def quickSort(start, end, nums):
    if start >= end:
        return

    left, right = start, end
    pivot = nums[(left + right) // 2]

    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    quickSort(start, right, nums)
    quickSort(left, end, nums)


if __name__ == "__main__":
    lists = [
        [2, 9, 8, 5, 3, 4, 7, 6],
    ]

    for alist in lists:
        print(sortArray(alist))
