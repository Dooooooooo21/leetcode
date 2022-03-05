#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 22:18
# @Author  : dly
# @File    : 49.py
# @Desc:
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        a, b, c = 0, 0, 0

        n2, n3, n5 = 0, 0, 0
        for i in range(1, n):
            n2 = dp[a] * 2
            n3 = dp[b] * 3
            n5 = dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            elif dp[i] == n3:
                b += 1
            elif dp[i] == n5:
                c += 1
        print(dp[-1])
        return dp[-1]


s = Solution()
s.nthUglyNumber(11)
