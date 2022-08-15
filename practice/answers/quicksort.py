def partitioning(nums, left, right):
    pivot = nums[right]
    start = left - 1
    for j in range(left, right):
        if nums[j] <= pivot:
            start += 1
            nums[start], nums[j] = nums[j], nums[start]
    nums[start + 1], nums[right] = nums[right], nums[start + 1]

    return start + 1


def quick_sort(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    if end <= start:
        return
    pivot = partitioning(nums, start, end)
    quick_sort(nums, start, pivot - 1)
    quick_sort(nums, pivot + 1, end)


if __name__ == "__main__":
    alist = [7, 6, 5, 1, 2, 3, 4, 2, 0, 9]
    quick_sort(alist)
    print(alist)
