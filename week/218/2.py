#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 10:46
# @Author  : dly
# @File    : 2.py
# @Desc    :

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        l = 0
        r = len(nums) - 1

        if r == 0:
            return []

        while l < r:
            tmp = k - nums[l]
            if tmp == nums[r]:
                count += 1
                l += 1
                r -= 1
            elif tmp > nums[r]:
                l += 1
            elif tmp < nums[r]:
                r -= 1

        return count


s = Solution()
res = s.maxOperations([3, 1, 3, 4, 3], 6)
print(res)
