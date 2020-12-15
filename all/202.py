#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 23:11
# @Author  : dly
# @File    : 202.py
# @Desc    :

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = [1]

        while n not in seen:
            seen.append(n)
            n = sum(int(i) ** 2 for i in str(n))

        return n == 1
