#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 10:32
# @Author  : dly
# @File    : 1.py
# @Desc    :
import re


class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """



        a = re.findall(r'1+', s)

        b = re.findall(r'0+', s)

        if len(a) == 0:
            return False
        if len(b) == 0:
            return True

        if len(max(a)) > len(max(b)):
            return True

        return False


s = Solution()
s.checkZeroOnes('1')
