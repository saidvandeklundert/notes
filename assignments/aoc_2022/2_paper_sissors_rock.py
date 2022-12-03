"""
X for Rock, Y for Paper, and Z for Scissors.

the score for a single round is the score for the shape you selected 
  (1 for Rock, 2 for Paper, and 3 for Scissors) 
  
plus the score for the outcome of the round 
 (0 if you lost, 3 if the round was a draw, and 6 if you won)

Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. 

 If both players choose the same shape, the round instead ends in a draw.    

 Opponent:
 A for Rock, B for Paper, and C for Scissors 
"""
from enum import Enum


def match_result(opponent, me) -> int:
    opponent_choice = selection_table[opponent]
    my_choice = selection_table[me]
    if my_choice == opponent_choice:
        return 3
    if my_choice == Choice.ROCK and opponent_choice == Choice.SCISSORS:
        return 6
    if my_choice == Choice.SCISSORS and opponent_choice == Choice.PAPER:
        return 6
    if my_choice == Choice.PAPER and opponent_choice == Choice.ROCK:
        return 6
    return 0


class Choice(Enum):
    ROCK = "rock"
    SCISSORS = "scissorts"
    PAPER = "paper"


selection_worth = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
win_worth = {"win": 6, "draw": 3, "lose": 0}
selection_worth_enum = {Choice.ROCK: 1, Choice.PAPER: 2, Choice.SCISSORS: 3}
selection_table = {
    "X": Choice.ROCK,
    "Y": Choice.PAPER,
    "Z": Choice.SCISSORS,
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
}
TOTAL_SCORE = 0
input_data: list[tuple[str, str]] = []
with open("input_2.txt", "rt") as f:
    for line in f.readlines():
        data = line.strip()
        chunks = data.split(" ")
        input_data.append((chunks[0], chunks[1]))

# calculate score:
for round in input_data:
    TOTAL_SCORE += selection_worth[round[1]]
    match_points = match_result(round[0], round[1])
    TOTAL_SCORE += match_points


print(TOTAL_SCORE)

# round 2:
# X means you need to lose,
# Y means you need to end the round in a draw, a
# Z means you need to win. Good luck!"

# win_worth = {"win": 6, "draw": 3, "lose": 0}

# (1 for Rock, 2 for Paper, and 3 for Scissors)

#    "A": Choice.ROCK,
# "B": Choice.PAPER,
#   "C": Choice.SCISSORS,


def rock_paper_scissors(file):
    total = 0
    hand_values = {
        "A": {
            "X": 3,  # i need to lose from rock, so I pick sisors. Lose + sisors = 3
            "Y": 4,  # i need to even with rock, so I pick rock. even + rock = 4
            "Z": 8,
        },
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7},
    }
    with open(file) as games:
        for line in games:
            hands = line.splitlines()[0].split(" ")
            total += hand_values[hands[0]][hands[1]]
    return total


print(f"Total score: {rock_paper_scissors('input_2.txt')}")
