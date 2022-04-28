from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            seen = count_dict.get(num)

            if seen:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        number_of_times_seen = 0
        number_seen_the_most = 0
        for key, value in count_dict.items():
            if value > number_of_times_seen:
                number_of_times_seen = value
                number_seen_the_most = key
            else:
                continue
        return number_seen_the_most


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == "__main__":
    alist = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
    ]
    for x in alist:
        print(Solution().majorityElement(x))
