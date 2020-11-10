#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 22:57
# @Author  : dly
# @File    : 65.py
# @Desc    : 位运算

class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = a ^ b, (a & b) << 1 & x

        return a if a <= 0x7fffffff else ~(a ^ x)


print(Solution().add(1, 2))
