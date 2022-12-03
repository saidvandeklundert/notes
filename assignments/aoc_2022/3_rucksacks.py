import string

data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""  # should sum up to 157
with open("input_3.txt", "rt") as f:
    data = f.read()

value_mapping = {}

for number, item in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1):
    value_mapping[item] = number


def two_halves(s: str) -> tuple[str, str]:
    half = len(s) // 2
    return (s[0:half:], s[half::])


def find_similar(s1: str, s2: str) -> str:
    for letter in s1:
        if letter in s2:
            return letter
    else:
        raise RuntimeError("something is wrong")


TOTAL = 0
for line in data.splitlines():
    halves = two_halves(line)
    similar = find_similar(halves[0], halves[1])
    TOTAL += value_mapping[similar]

print(f"answer to section 1: {TOTAL}")

# group every three lines
# find common letter in all three lines and look up value
# add all values together
data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""  # should produce 70
with open("input_3.txt", "rt") as f:
    data = f.read()

groups = []
addition = []
for line in data.splitlines():
    if len(addition) == 3:
        groups.append(addition)
        addition = []
    addition.append(line)
else:
    if len(addition) == 3:
        groups.append(addition)
        addition = []


def find_similar_in_lists(l: list[list[str]]) -> str:
    for item in l[0]:
        if item in l[1]:
            if item in l[2]:
                return item
    raise RuntimeError("nothing was found")


TOTAL_2 = 0
for grouping in groups:
    TOTAL_2 += value_mapping[find_similar_in_lists(grouping)]
print(f"answer to section 2: {TOTAL_2}")
