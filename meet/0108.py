#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 22:51
# @Author  : dly
# @File    : 0108.py
# @Desc    :

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix

        row = set()
        line = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    line.add(j)

        for num in row:
            matrix[num] = [0] * len(matrix[0])
        for num in line:
            for i in range(len(matrix)):
                matrix[i][num] = 0

        return matrix


s = Solution()
s.setZeroes([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
])
