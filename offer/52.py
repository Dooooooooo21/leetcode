#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 22:18
# @Author  : dly
# @File    : 52.py
# @Desc    :

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = 0
        b = 0
        ha = headA
        hb = headB

        while ha:
            a += 1
            ha = ha.next

        while hb:
            b += 1
            hb = hb.next

        count = 0
        if a > b:
            while count < a - b:
                headA = headA.next
                count += 1
        elif b > a:
            while count < b - a:
                headB = headB.next
                count += 1

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None
