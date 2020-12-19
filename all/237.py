#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 21:22
# @Author  : dly
# @File    : 237.py
# @Desc    :

# 原地删除节点
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next
