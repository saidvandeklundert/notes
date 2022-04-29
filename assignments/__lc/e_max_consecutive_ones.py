from typing import List


class Solution:
    """horrible"""

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_count = 0
        curr_count = 0
        for number in nums:

            if number == 1:
                curr_count += 1
            else:
                # if curr_count is biggern then max_count, use curr_count
                if curr_count > max_count:
                    max_count = curr_count

                # reset curr_count
                curr_count = 0
        else:
            # if curr_count is biggern then max_count, use curr_count
            if curr_count > max_count:
                max_count = curr_count
        return max_count


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        cnt = 0
        ans = 0
        for number in nums:
            if number == 1:
                cnt += 1
                ans = ans if ans > cnt else cnt
            else:
                cnt = 0
        return ans


if __name__ == "__main__":
    alist = [[1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1]]
    for x in alist:
        print(Solution().findMaxConsecutiveOnes(x))
