from turtle import right


def sum_divide_and_conquer(numbers: list[int]):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        mid = len(numbers) // 2
        left_half = sum_divide_and_conquer(numbers[0:mid])
        right_half = sum_divide_and_conquer(numbers[mid : len(numbers) + 1])
    return left_half + right_half


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(sum_divide_and_conquer(nums))
