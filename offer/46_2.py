#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 20:48
# @Author  : dly
# @File    : 46_2.py
# @Desc:

class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        a = b = 1

        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if '10' <= tmp <= '26' else a
            b = a
            a = c

        return a
