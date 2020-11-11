#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:47
# @Author  : dly
# @File    : 3.py
# @Desc    :

# 无重复字符的最长子串
# 滑动窗口
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = len(s)
        repeat = []
        maxlen = 0

        for i in range(l):
            while s[i] in repeat:
                repeat.pop(0)
            repeat.append(s[i])
            if len(repeat) > maxlen:
                maxlen = len(repeat)

        return maxlen