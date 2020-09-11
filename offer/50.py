#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 22:08
# @Author  : dly
# @File    : 50.py
# @Desc:

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}

        for c in s:
            dic[c] = not c in dic

        print(dic)

        for c in s:
            if dic[c]:
                return c

        return ' '


s = Solution()
s.firstUniqChar('leetcode')
