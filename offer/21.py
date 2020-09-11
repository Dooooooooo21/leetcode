import collections


class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1

        while i + 1 <= j:
            if nums[i] & 1 == 0 and nums[j] & 1 == 1:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
                continue
            elif nums[i] & 1 == 1:
                i += 1
            elif nums[j] & 1 == 0:
                j -= 1

        return nums


nums = [1, 2, 3, 4]
s = Solution()
print(s.exchange(nums))
