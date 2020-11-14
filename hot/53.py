#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 23:08
# @Author  : dly
# @File    : 53.py
# @Desc    :

# 具有最大和的连续子数组
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        ans = nums[0]
        tmp = nums[0]
        i = 1
        while i < len(nums):
            if tmp < 0:
                tmp = 0
                continue
            tmp += nums[i]
            i += 1
            if tmp > ans:
                ans = tmp
        return ans


s = Solution()
s.maxSubArray([-2, 1])
