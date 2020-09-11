#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 21:58
# @Author  : dly
# @File    : 47.py
# @Desc:

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = grid

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    dp[i][j] += grid[i][j - 1]
                elif i != 0 and j == 0:
                    dp[i][j] += grid[i - 1][j]
                else:
                    dp[i][j] += max(grid[i][j - 1], grid[i - 1][j])

        return dp[-1][-1]
