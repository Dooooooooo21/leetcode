#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 14:41
# @Author  : dly
# @File    : 142.py
# @Desc    :

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return fast
