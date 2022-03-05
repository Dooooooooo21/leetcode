#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 11:03
# @Author  : dly
# @File    : 2.py
# @Desc    :

from math import ceil


class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        if len(dist) > ceil(hour):
            return -1

        max_speed = max(dist) * 100 + 1

        for i in range(1, max_speed):
            use_hour = 0
            for dis in dist[:-1]:
                use_hour += ceil(dis / i)
            use_hour += dist[-1] / i
            if use_hour <= hour:
                return i

        return -1


s = Solution()
print(s.minSpeedOnTime([1, 1, 1000000], 2.01))
