class Solution(object):
    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, start, end):
        if end <= start:
            return
        mid = (start + end) // 2
        nums[start], nums[mid] = nums[mid], nums[start]
        i = start + 1
        j = end
        while i <= j:
            while i <= j and nums[i] <= nums[start]:
                i += 1
            while i <= j and nums[j] >= nums[start]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[j] = nums[j], nums[start]
        self.quickSort(nums, start, j - 1)
        self.quickSort(nums, j + 1, end)


class Solution2(object):
    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, start, end):
        if end <= start:
            return
        pivot = partitioning(nums, start, end)

        self.quickSort(nums, start, pivot - 1)
        self.quickSort(nums, pivot + 1, end)


def partitioning(nums, left, right):
    pivot = nums[right]
    start = left - 1
    for j in range(left, right):
        if nums[j] <= pivot:
            start += 1
            nums[start], nums[j] = nums[j], nums[start]
    nums[start + 1], nums[right] = nums[right], nums[start + 1]
    return start + 1


def sortArray_1(nums):
    quickSort1(nums, 0, len(nums) - 1)
    return nums


def quickSort1(nums, start, end):
    if end <= start:
        return
    mid = (start + end) // 2
    nums[start], nums[mid] = nums[mid], nums[start]
    i = start + 1
    j = end
    while i <= j:
        while i <= j and nums[i] <= nums[start]:
            i += 1
        while i <= j and nums[j] >= nums[start]:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[start], nums[j] = nums[j], nums[start]
    quickSort1(nums, start, j - 1)
    quickSort1(nums, j + 1, end)


def sortArray2(nums):
    quickSort(nums, 0, len(nums) - 1)
    return nums


def partitioning1(nums, left, right):
    pivot = nums[right]
    start = left - 1
    for j in range(left, right):
        if nums[j] <= pivot:
            start += 1
            nums[start], nums[j] = nums[j], nums[start]
    nums[start + 1], nums[right] = nums[right], nums[start + 1]
    return start + 1


def quickSort(nums, start, end):
    if end <= start:
        return
    pivot = partitioning1(nums, start, end)
    quickSort(nums, start, pivot - 1)
    quickSort(nums, pivot + 1, end)
