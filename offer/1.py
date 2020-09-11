class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            m = i
            s = num
            # if s > target:
            #     continue

            for j in range(i + 1, len(nums)):
                s += nums[j]
                if s == target:
                    n = j
                    return [m, n]
                else:
                    s -= nums[j]


nums = [-1, -2, -3, -4, -5]
s = Solution()
print(s.twoSum(nums, -8))
