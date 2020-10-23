#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 22:08
# @Author  : dly
# @File    : 56_1.py
# @Desc    :

class Solution(object):
    def singleNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = 0
        a = 0
        b = 0

        for num in nums:
            res ^= num

        h = 1
        while res & h == 0:
            h <<= 1

        for num in nums:
            if num & h == 0:
                a ^= num
            else:
                b ^= num

        print(a, b)
        return [a, b]


Solution.singleNumbers([4, 1, 4, 7])
