#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 23:16
# @Author  : dly
# @File    : 57.py
# @Desc    :

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1

        if r == 0:
            return []

        while l <= r:
            tmp = target - nums[l]
            if tmp == nums[r]:
                return [nums[l], nums[r]]
            elif tmp > nums[r]:
                l += 1
            elif tmp < nums[r]:
                r -= 1

        return []
