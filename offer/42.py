#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 22:01
# @Author  : dly
# @File    : 42.py
# @Desc:

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        sum = max = nums[0]

        for i in range(len(nums) - 1):
            if sum >= 0:
                sum += nums[i + 1]
            else:
                sum = nums[i + 1]
            if sum > max:
                max = sum

        return max
