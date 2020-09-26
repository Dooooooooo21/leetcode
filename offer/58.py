#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 23:20
# @Author  : dly
# @File    : 58.py
# @Desc    :


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        list = s.split()
        list.reverse()

        return ' '.join(list)
