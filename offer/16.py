class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def result(base, nc):
            if nc == 1:
                return base
            num = result(base, nc >> 1)
            if nc % 2 == 0:
                return num * num
            else:
                return num * num * x

        if n == 0:
            return 1
        elif n < 0:
            return 1. / result(x, -n)

        return result(x, n)


s = Solution()
print(s.myPow(2, 10))
