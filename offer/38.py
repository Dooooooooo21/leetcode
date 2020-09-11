#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 22:25
# @Author  : dly
# @File    : 38.py
# @Desc:


class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        c = list(s)

        def dfs(index):
            if index == len(c) - 1:
                res.append(''.join(c))
                return
            help = set()
            for i in range(index, len(c)):
                if c[i] in help:
                    continue
                help.add(c[i])
                c[i], c[index] = c[index], c[i]
                dfs(index + 1)
                c[index], c[i] = c[i], c[index]

        dfs(0)
        return res
