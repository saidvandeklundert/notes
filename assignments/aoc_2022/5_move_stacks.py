from dataclasses import dataclass
from collections import deque


@dataclass
class Instruction:
    number: int
    source: int
    dest: int


sample_input = """ 
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

with open("input_5.txt", "rt") as f:
    full_data_input = f.read()


def get_moves(data: str) -> list[Instruction]:

    return_value = []
    for line in data.splitlines():
        if line.startswith("move"):
            chunks = line.split(" ")
            source = int(chunks[3]) - 1
            dest = int(chunks[5]) - 1
            return_value.append(
                Instruction(number=int(chunks[1]), source=source, dest=dest)
            )
    return return_value


def get_stacks(data: str):
    """
    Return the stacks from the input string:

        [D]
    [N] [C]
    [Z] [M] [P]
    1   2   3

    """
    return_value = [deque() for x in range(9)]
    for line in data.splitlines():
        if "[" in line:
            line_length = len(line)
            idx = 0
            while idx < line_length:
                if line[idx].isalpha():
                    letter = line[idx]
                    stack_num = idx // 4
                    return_value[stack_num].append(letter)
                idx += 1

    return return_value


def display_text_bottom_of_stack(data_input):
    moves = get_moves(data_input)
    stacks = get_stacks(data_input)
    print(moves)
    print("start", stacks)
    for move in moves:
        print("\n\t", move)

        for _ in range(move.number):
            item = stacks[move.source].popleft()
            stacks[move.dest].appendleft(item)
        print("\t", stacks)
    answer = ""
    for s in stacks:
        if s:
            answer += s.popleft()
    print(answer)


# display_text_bottom_of_stack(sample_input)


def display_text_bottom_of_stack_ng_mover(data_input):
    """
        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

     to MCD
    """
    moves = get_moves(data_input)
    stacks = get_stacks(data_input)
    print(moves)
    print("start", stacks)
    for move in moves:
        print("\n\t", move)

        if move.number == len(stacks[move.source]):
            print("MOVE the entire stack!")

            for _ in range(move.number):
                item = stacks[move.source].pop()
                print("move  ", item, "to ", move.dest, stacks[move.dest])
                stacks[move.dest].appendleft(item)
                print("now  ", stacks[move.dest])

            print("now  ", stacks[move.dest])
        else:
            for _ in range(move.number):
                item = stacks[move.source].popleft()
                print("move  ", item, "to ", move.dest, stacks[move.dest])
                stacks[move.dest].appendleft(item)
                print("now  ", stacks[move.dest])
        # print("\n\n\t\tNow the stacks are:\n\n", stacks, "\n")
    print(stacks)
    answer = ""
    for s in stacks:
        if s:
            answer += s[0]
    print(answer)


# sample_input
# full_data_input
# not BTGSHQRCJ
# BNTZFPMMW
display_text_bottom_of_stack_ng_mover(full_data_input)
