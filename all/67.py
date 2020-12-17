#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 22:02
# @Author  : dly
# @File    : 67.py
# @Desc    :

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2)))[2:]
