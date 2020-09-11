#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 21:38
# @Author  : dly
# @File    : 136.py
# @Desc:

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]

        for i in range(1, len(nums)):
            result ^= nums[i]

        return result


print(Solution().singleNumber([2, 2, 7, 3, 1, 1, 7]))
