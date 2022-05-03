from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        checker = [x for x in heights]
        print(heights)
        print(checker)
        checker.sort()
        wrong = 0
        for index, value in enumerate(checker):
            if heights[index] != value:
                wrong += 1
            else:
                pass
        return wrong


alist = [[1, 1, 4, 2, 1, 3], [5, 1, 2, 3, 4], [1, 2, 3, 4, 5]]

for heights in alist:
    print(Solution().heightChecker(heights=heights))
