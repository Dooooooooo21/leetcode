#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 21:08
# @Author  : dly
# @File    : 29.py
# @Desc:

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        res = []
        while l <= r and t <= b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in reversed(range(l, r + 1)):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in reversed(range(t, b + 1)):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break

        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.spiralOrder(matrix))
