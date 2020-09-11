#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 21:00
# @Author  : dly
# @File    : 48.py
# @Desc:
import collections


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        low = 0
        result = 0

        for high in range(len(s)):
            if s[high] not in s[low:high]:
                result = max(result, high - low + 1)
            else:
                while s[high] in s[low:high]:
                    low += 1

        return result


print(Solution().lengthOfLongestSubstring('abcabcbb'))
