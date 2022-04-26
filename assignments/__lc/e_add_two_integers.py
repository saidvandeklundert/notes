class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # print(num1, num2)
        return num1 + num2


if __name__ == "__main__":
    alist = [
        (12, 5),
        (-10, 4),
    ]
    for t in alist:
        print(Solution().sum(t[0], t[1]))
