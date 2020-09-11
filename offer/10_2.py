class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n == 2:
            return 2

        l = 1
        m = 2
        h = 0

        for i in range(2, n):
            h = (m + l) % 1000000007
            l = m
            m = h

        return h


s = Solution()
print(s.numWays(0))
