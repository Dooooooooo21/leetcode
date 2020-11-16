#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 21:17
# @Author  : dly
# @File    : 139.py
# @Desc    :

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        for i in range(size):
            for j in range(i + 1, size + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True

        return dp[-1]
