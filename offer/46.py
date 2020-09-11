#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 20:42
# @Author  : dly
# @File    : 46.py
# @Desc:

class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9:
            return 1
        tmp = num % 100
        if tmp <= 9 or tmp >= 26:
            return self.translateNum(num // 10)
        else:
            return self.translateNum(num // 10) + self.translateNum(num // 100)


print(Solution().translateNum(12258))
