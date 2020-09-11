#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 22:21
# @Author  : dly
# @File    : 39.py
# @Desc:

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        return nums[len(nums) // 2]
