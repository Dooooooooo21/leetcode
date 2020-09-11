class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return list(range(1, 10 ** n))


solution = Solution()
print(solution.printNumbers(1))
