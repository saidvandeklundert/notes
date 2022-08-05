from data import arrays
import copy


def bubble_sort(array: list[int]) -> None:
    array_len = len(array) - 1
    for i in range(array_len):
        for j in range(array_len - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def sortArray(nums: list[int]):
    array_len = len(nums) - 1
    # for every index in the array:
    for i in range(array_len):
        # for every index minus the index we are working:
        for idx in range(array_len - i):
            # swap the number if the next number is bigger
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]


if __name__ == "__main__":
    for array in arrays:
        a_1 = copy.copy(array)
        a_2 = copy.copy(array)
        if len(a_1) < 20:
            print(a_1)
        bubble_sort(array=a_1)
        if len(a_1) < 20:
            print(a_1)
        if len(a_2) < 20:
            print(a_2)
        sortArray(a_2)
        if len(a_2) < 20:
            print(a_2)
