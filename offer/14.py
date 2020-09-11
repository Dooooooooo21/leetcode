class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        result = [0] * (n + 1)
        result[1] = 1
        result[2] = 2
        result[3] = 3

        for i in range(4, n + 1):
            for j in range(1, i // 2 + 1):
                result[i] = max(result[i], result[j] * result[i - j])
        return result[-1] % 1000000007


s = Solution()
print(s.cuttingRope(127))
