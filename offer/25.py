#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 14:42
# @Author  : dly
# @File    : 25.py
# @Desc:


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result = ListNode(0)
        head = result
        while l1 and l2:
            if l1.val == l2.val:
                head.next = ListNode(l1.val)
                head = head.next
                head.next = ListNode(l2.val)
                head = head.next

                l1 = l1.next
                l2 = l2.next
            elif l1.val < l2.val:
                head.next = ListNode(l1.val)
                head = head.next

                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next

        if l1 is None:
            head.next = l2
        if l2 is None:
            head.next = l1

        return result.next


l = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)

l.next = l2
l2.next = l3

n = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(4)
n.next = n2
n2.next = n3

s = Solution()
res = s.mergeTwoLists(l, n)
while res:
    print(res.val)
    res = res.next
