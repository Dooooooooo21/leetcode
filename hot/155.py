#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 23:42
# @Author  : dly
# @File    : 155.py
# @Desc    :

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        self.mini = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.queue:
            self.mini.append(x)
        else:
            mi = self.mini[-1]
            self.mini.append(min(mi, x))
        self.queue.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.mini.pop(-1)
        return self.queue.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini[-1]