def aoc_1():
    count = 0
    previous_value = 0

    with open("input.txt") as f:
        lines = f.readlines()

    for line in lines:
        line_value = int(line.strip())
        if previous_value == 0:
            previous_value = line_value
            continue
        elif line_value > previous_value:
            count += 1
        previous_value = line_value
    print(f"descended {count} times")


def aoc_2():
    with open("input.txt") as f:
        lines = f.readlines()
    count = 0
    previous_window = 0
    window_size = 3
    lines_length = len(lines)
    i = 0
    while i < lines_length:
        curr_lines = lines[i : i + window_size]
        curr_lines = [int(x) for x in curr_lines]
        i += 1
        curr_window = sum(curr_lines)
        if curr_window > previous_window and previous_window != 0:
            count += 1
        previous_window = curr_window
    print(f"window increases: {count}")


if __name__ == "__main__":

    aoc_1()
    aoc_2()