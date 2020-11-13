#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 21:56
# @Author  : dly
# @File    : 11.py
# @Desc    :


# 盛水最多的容器
# 双指针
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1

        m = 0
        while l <= r:
            m = max(m, min(height[r], height[l]) * (r - l))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        print(m)
        return m


s = Solution()
s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
