#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 22:32
# @Author  : dly
# @File    : 0302.py
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
        if not self.queue:
            return -1
        else:
            self.mini.pop(-1)
            return self.queue.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if not self.queue:
            return -1
        else:
            return self.queue[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.queue:
            return -1
        else:
            return self.mini[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()

