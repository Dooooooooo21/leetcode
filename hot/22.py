#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 23:00
# @Author  : dly
# @File    : 22.py
# @Desc    :

# 有效的括号
# 回溯
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        res = []

        def dfs(l, r, tmp):
            if l == 0 and r == 0:
                res.append(tmp)
                return
            if l > 0:
                dfs(l - 1, r, tmp + '(')
            if l < r:
                dfs(l, r - 1, tmp + ')')

        dfs(n, n, '')
        return res
