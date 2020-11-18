#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 22:33
# @Author  : dly
# @File    : 283.py
# @Desc    :

# 移动零
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums
