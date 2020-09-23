#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 23:28
# @Author  : dly
# @File    : 57_2.py
# @Desc    :

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """

        if target < 3:
            return []

        l = 1
        r = 2
        middle = (target + 1) // 2
        sum = l + r
        result = []

        while l < middle:
            if sum == target:
                result.append(list(range(l,r)))
                sum -= l
                l += 1
            elif sum < target:
                r += 1
                sum += r
            elif sum > target:
                sum -= l
                l += 1

        return result


Solution().findContinuousSequence(15)
