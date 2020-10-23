#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 21:40
# @Author  : dly
# @File    : 11.py
# @Desc    :

class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        l = 0
        r = len(numbers) - 1

        while l < r:
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                return min(numbers[l:r])

        return numbers[l]
