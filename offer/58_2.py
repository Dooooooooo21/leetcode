#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 23:31
# @Author  : dly
# @File    : 58_2.py
# @Desc    :
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """

        return s[n:].join(s[:n])
