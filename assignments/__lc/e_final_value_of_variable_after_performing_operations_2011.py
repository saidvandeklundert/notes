from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return_value = 0
        ops = {
            "--X": -1,
            "X++": +1,
            "++X": +1,
            "X--": -1,
        }
        for op in operations:
            return_value = return_value + ops[op]

        return return_value


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([op for op in map(lambda op: 1 if op[1] == "+" else -1, operations)])


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i] == "X++":
                x += 1
            else:
                x -= 1
        return x


alist = [["--X", "X++", "X++"], ["++X", "++X", "X++"]]
for x in alist:
    print(Solution().finalValueAfterOperations(x))
