def assignment_input() -> list[str]:
    assignment_input: list[str] = []

    with open("input_1.txt", "rt") as f:
        for line in f.readlines():
            assignment_input.append(line)
    return assignment_input


def elf_with_most_calories(assignment_input: list[str]) -> int:
    """
    Elves in the input data are carrying food.

    Return the amount of calories carried by the elf that is
    carrying the most
    """
    highest = 0
    curr_cal = 0
    for item in assignment_input:
        if item[0].isdigit():
            curr_cal += int(item.strip())
        else:
            curr_cal = 0
        if curr_cal > highest:
            highest = curr_cal

    return highest


def sum_of_three_highest_values(assignment_input: list[str]) -> int:
    """
    Elves in the input data are carrying food.

    Return the amount of calories carried by the elf that is
    carrying the most
    """
    elves_calories: list[int] = []
    curr_cal = 0
    for item in assignment_input:
        if item[0].isdigit():
            curr_cal += int(item.strip())
        else:
            elves_calories.append(curr_cal)
            curr_cal = 0

    return sum(elves_calories[-3:])


print(elf_with_most_calories(assignment_input=assignment_input()))
print(sum_of_three_highest_values(assignment_input=assignment_input()))
