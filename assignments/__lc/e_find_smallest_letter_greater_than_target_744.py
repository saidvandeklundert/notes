import bisect


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect_right(letters, target)
        print("bisect result", index)
        answer_idx = index % len(letters)
        print(f"answer_idx: {answer_idx}")
        return letters[answer_idx]


alist = [
    [["c", "f", "j"], "a"],  # c
    [["c", "f", "j"], "c"],  # f
    [["c", "f", "j"], "d"],  # f
    [["c", "f", "j"], "k"],
    [["c", "f", "j"], "j"],
    [["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e"],  # n
    [["c", "f", "j"], "z"],  # c
]

for l in alist:
    print(Solution().nextGreatestLetter(l[0], l[1]))
