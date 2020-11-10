#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 22:57
# @Author  : dly
# @File    : 61.py
# @Desc    : 是否为顺子，max - min < 5

class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ma, mi = 0, 14
        repeat = set()

        for num in nums:
            if num == 0:
                continue
            if num in repeat:
                return False
            repeat.add(num)
            ma = max(ma, num)
            mi = min(mi, num)

        return ma - mi < 5
