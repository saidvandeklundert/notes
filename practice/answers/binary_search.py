def binary_search(array: list[int], target: int) -> int:
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            high = middle - 1
        elif array[middle] < target:
            low = middle + 1

    return -1
