#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 22:37
# @Author  : dly
# @File    : 19.py
# @Desc:

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = cur = head

        i = 0
        while i < n - 1:
            cur = cur.next
            i += 1
        while cur:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next

        return head
