#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 23:01
# @Author  : dly
# @File    : 62.py
# @Desc    :

import math


# 不同路径
class Solution(object):
    # 排列组合
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

    # 动态规划
    # 由于只能向左和向下 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
