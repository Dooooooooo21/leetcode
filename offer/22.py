# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return False

        first = second = head
        count = 0
        while second and count < k - 1:
            second = second.next
            count += 1
        while second and second.next:
            second = second.next
            first = first.next

        return first
