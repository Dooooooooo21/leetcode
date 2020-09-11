# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        fhead = ListNode(0)
        fhead.next = head

        pre = fhead
        cur = fhead.next

        while True:
            if cur.val == val:
                pre.next = cur.next
                break
            pre = pre.next
            cur = cur.next

        return fhead.next
