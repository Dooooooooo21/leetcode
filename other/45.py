#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 22:17
# @Author  : dly
# @File    : 45.py
# @Desc    :


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        ans = 0
        end = 0
        maxPos = 0
        for i in range(len(nums) - 1):
            maxPos = max(i + nums[i], maxPos)
            if i == end:
                end = maxPos
                ans += 1

        return ans


s = Solution()
s.jump([2, 3, 1, 1, 4])
