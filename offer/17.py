class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return list(range(1, 10 ** n))

    def printNumbers2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def dfs(x):
            if x == n:
                tmp = ''.join(num[self.start:])
                if tmp != '0': res.append(int(tmp))
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        self.nine = 0
        self.start = n - 1
        num = ['0'] * n
        res = []
        dfs(0)

        return res


solution = Solution()
print(solution.printNumbers2(2))
