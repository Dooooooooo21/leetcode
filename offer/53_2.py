#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 21:34
# @Author  : dly
# @File    : 53_2.py
# @Desc:

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1

        while i <= j:
            m = (j + i) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1

        return i
