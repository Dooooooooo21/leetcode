#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 21:14
# @Author  : dly
# @File    : 160.py
# @Desc    :

# 两链表相交的起始节点
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        ta = headA
        a = 0
        while ta:
            ta = ta.next
            a += 1

        tb = headB
        b = 0
        while tb:
            tb = tb.next
            b += 1

        tmp = a - b
        while tmp < 0:
            headB = headB.next
            tmp += 1
        while tmp > 0:
            headA = headA.next
            tmp -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
