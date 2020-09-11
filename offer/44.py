#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 21:08
# @Author  : dly
# @File    : 44.py
# @Desc:


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        digit = 1
        start = 1
        count = 9

        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit

        num = start + (n - 1) // digit

        return int(str(num)[(n - 1) % digit])


s = Solution()
s.findNthDigit(11)
