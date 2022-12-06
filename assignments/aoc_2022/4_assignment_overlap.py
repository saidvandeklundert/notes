sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
with open("input_4.txt", "rt") as f:
    full_input = f.read()


def sanitize_input(input_data: str) -> list[tuple[int, int, int, int]]:
    """
    Transform input data to a list of tuples that
    contain 4 numbers
    """
    return_list: list[tuple[int, int, int, int]] = []
    for line in input_data.splitlines():

        halves = line.split(",")
        addition: list[int] = []
        for half in halves:

            numbers = half.split("-")
            addition.append(int(numbers[0]))
            addition.append(int(numbers[1]))

        return_list.append(tuple(addition))
    return return_list


def is_contained(series: tuple[int, int, int, int]) -> bool:
    if series[0] <= series[2] and series[1] >= series[3]:
        return True
    elif series[1] <= series[3] and series[0] >= series[2]:
        return True
    return False


def overlap_count(input_data: str) -> int:
    """number of instance where either of the two number
    ranges is fully contained in the other.


    """
    overlap_count = 0
    sanitized_data = sanitize_input(input_data)
    for item in sanitized_data:
        if is_contained(item):
            overlap_count += 1
        else:
            # print("no overlap")
            # print(item)
            pass
    print(f"the times there is overlap is {overlap_count}")
    return overlap_count


overlap_count(sample)
overlap_count(input_data=full_input)


def partialy_contained(series: tuple[int, int, int, int]) -> bool:
    """
    2-4,6-8 > False
    2-3,4-5 > False
    5-7,7-9 > True
    2-8,3-7 > True
    6-6,4-6 > True
    2-6,4-8 > True
    """
    if series[0] >= series[2] and series[0] <= series[3]:
        return True
    elif series[1] >= series[2] and series[0] <= series[3]:
        return True
    return False


def partial_overlap_count(input_data: str) -> int:
    partial_overlap_count = 0
    sanitized_data = sanitize_input(input_data)
    for series in sanitized_data:
        if partialy_contained(series):
            partial_overlap_count += 1
    print(f"the times there is overlap is {partial_overlap_count}")
    return partial_overlap_count


partial_overlap_count(sample)

partial_overlap_count(full_input)
