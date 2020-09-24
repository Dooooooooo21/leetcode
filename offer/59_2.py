#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 22:21
# @Author  : dly
# @File    : 59_2.py
# @Desc    :

import collections


class MaxQueue(object):

    def __init__(self):
        self.max_queue = collections.deque()
        self.queue = collections.deque()

    def max_value(self):
        """
        :rtype: int
        """
        if not self.max_queue:
            return -1

        return self.max_queue[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queue:
            return -1

        value = self.queue.popleft()
        if value == self.max_queue[0]:
            self.max_queue.popleft()

        return value
