#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 23:22
# @Author  : dly
# @File    : 64.py
# @Desc    :

# dp
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        line = len(grid[0])
        dp = [[0 for _ in range(line)] for _ in range(row)]
        # print(dp)

        dp[0][0] = grid[0][0]

        for i in range(row):
            for j in range(line):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[-1][-1]


s = Solution()
s.minPathSum([[1, 2, 3], [4, 5, 6]])
