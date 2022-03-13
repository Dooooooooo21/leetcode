#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 11:05
# @Author  : dly
# @File    : 5227.py
# @Desc    :

class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return nums[0]

        n = len(nums)
        if n == 1 and k % 2 == 1:
            return -1

        if k < n:
            return max(nums[k], max([0] + nums[:k - 1]))

        if k == n:
            return max(nums[:k - 1])

        return max(nums)


s = Solution()
res = s.maximumTop(nums=[5, 2, 2, 4, 0, 6], k=4)
print(res)
