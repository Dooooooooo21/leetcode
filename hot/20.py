#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 22:51
# @Author  : dly
# @File    : 20.py
# @Desc    :

# 有效的括号
# 栈

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']

        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if dic[stack.pop()] != i:
                    return False

        return len(stack) == 1
