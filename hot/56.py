#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 22:35
# @Author  : dly
# @File    : 56.py
# @Desc    :

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])

        res = []

        for pair in intervals:
            if len(res) == 0 or res[-1][1] < pair[0]:
                res.append(pair)
            else:
                res[-1][1] = max(res[-1][1], pair[1])

        return res
