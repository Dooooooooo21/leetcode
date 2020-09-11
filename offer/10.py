class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        l = 0
        m = 1
        h = 0

        for i in range(1, n):
            h = (m + l) % 1000000007
            l = m
            m = h

        return h


s = Solution()
print(s.fib(81))
