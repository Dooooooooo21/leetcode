#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 14:24
# @Author  : dly
# @File    : 151.py
# @Desc    :

# 环形链表
# 快慢指针
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        first = head
        second = head.next
        while first != second:
            if not second or not second.next:
                return False
            first = first.next
            second = second.next.next

        return True
