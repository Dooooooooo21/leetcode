#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 20:09
# @Author  : dly
# @File    : 30.py
# @Desc:


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.help_list = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.help_list) == 0:
            self.help_list.append(x)
            self.stack.append(x)
        else:
            tmp = self.help_list[-1]
            if x > tmp:
                self.help_list.append(tmp)
                self.stack.append(x)
            else:
                self.help_list.append(x)
                self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        top = self.stack.pop(-1)
        self.help_list.pop(-1)

        return top

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.help_list[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
