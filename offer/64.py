#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 21:35
# @Author  : dly
# @File    : 64.py
# @Desc:

class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n and (n + self.sumNums(n - 1))


print(Solution().sumNums(100))
