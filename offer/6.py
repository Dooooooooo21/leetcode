class Solution:
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        cur = head
        values = []

        while cur:
            values.append(cur.val)
            cur = cur.next
        values.reverse()

        return values


input = [1, 2, 3]
s = "We are happy."

solution = Solution()
print(solution.reversePrint(head))
