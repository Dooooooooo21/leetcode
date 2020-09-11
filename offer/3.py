from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        counts = [0] * len(nums)

        for i in nums:
            counts[nums[i]] += 1

        for index, value in enumerate(counts):
            if value > 1:
                return nums[index]


input = [1, 2, 1]
s = Solution()
print(s.findRepeatNumber(input))
