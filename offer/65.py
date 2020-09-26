#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 22:57
# @Author  : dly
# @File    : 65.py
# @Desc    :

class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        list = [a, b]
        return sum(list)


print(Solution().add(1, 2))
