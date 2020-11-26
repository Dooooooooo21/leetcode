#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 22:31
# @Author  : dly
# @File    : 83.py
# @Desc    :

# 删除排序链表中的重复元素
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head