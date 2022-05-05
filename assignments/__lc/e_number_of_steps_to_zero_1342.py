class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0:
            pass
            mod = num % 2
            if mod == 0:
                num = num / 2
                counter += 1
            else:
                num -= 1
                counter += 1

        return counter


alist = [14, 8, 123]

for x in alist:
    print(Solution().numberOfSteps(x))
