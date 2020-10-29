#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 21:38
# @Author  : dly
# @File    : 3_1.py
# @Desc    :

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            if i == num:
                continue
            tmp = nums[i]
            if tmp == num:
                return num
            nums[i] = num
            nums[num] = tmp

