#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:57
# @Author  : dly
# @File    : 4.py
# @Desc    :

# 最长回文子串
# 中心扩散
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def recur(s, l, r):
            n = len(s)
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1

        if len(s) <= 1:
            return s

        r = len(s) - 1
        res = ''
        maxlen = 0
        for i in range(r):
            l1 = recur(s, i, i)
            l2 = recur(s, i, i + 1)
            m = max(l1, l2)
            if m > maxlen:
                maxlen = m
                left = i - (m - 1) // 2
                right = i + m // 2
                res = s[left:right + 1]
        return res


s = Solution()
s.longestPalindrome('bbad')
