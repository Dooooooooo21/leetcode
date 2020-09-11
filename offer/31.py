#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 20:55
# @Author  : dly
# @File    : 31.py
# @Desc:

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        tmp = []
        i = 0
        for top in pushed:
            tmp.append(top)
            while tmp and tmp[-1] == popped[i]:
                tmp.pop(-1)
                i += 1

        return len(tmp) == 0
