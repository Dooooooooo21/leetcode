#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 22:28
# @Author  : dly
# @File    : 17.py
# @Desc    :

# 电话号码的字母组合

class Solution(object):
    # 递归 + 回溯
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        res = []

        def dfs(tmp, index):
            if index == len(digits):
                res.append(tmp)
                return

            c = digits[index]
            letters = d[ord(c) - 48]

            for i in letters:
                dfs(tmp + i, index + 1)

        dfs('', 0)
        return res

    # 队列求解
    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        res = ['']

        for i in digits:
            size = len(res)
            letters = d[ord(i) - 48]
            for _ in range(size):
                tmp = res.pop(0)
                for j in letters:
                    res.append(tmp + j)
        return res
