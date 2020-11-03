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

    def lengthOfLongestSubstring2(self, s):
        i, n = 0, len(s)
        ans, h = 0, set()
        j = 0
        # for j in range(n):
        while j < n:
            if s[j] in h:
                i = i + 1
                j = i
                h.clear()

            h.add(s[j])
            ans = max(ans, j - i + 1)
            j += 1

        return ans


print(Solution().lengthOfLongestSubstring2('abcabcbb'))

for i in range(10):
    print(i)
    i += 1
