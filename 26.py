#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 11:19
# @Author  : dly
# @File    : 26.py
# @Desc:

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
