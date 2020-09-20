#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 20:48
# @Author  : dly
# @File    : 53.py
# @Desc    :

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        dict = {}
        for num in nums:
            if num in dict:
                count = dict.get(num)
                count += 1
                dict[num] = count
            else:
                dict[num] = 1

        if target in dict:
            return dict.get(target)
        else:
            return 0
