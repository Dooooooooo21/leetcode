class Solution(object):

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1

        flag = [[0] * n for i in range(m)]
        count = 0

        def sum(num):
            if num < 10:
                return num

            sum = num // 10 + num % 10

            return sum

        def dfs(i, j):
            nonlocal count
            if 0 <= i < m and 0 <= j < n and (sum(i) + sum((j))) <= k and not flag[i][j]:
                flag[i][j] = 1
                count += 1
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        dfs(0, 0)
        return count


m = 3
n = 1
k = 0
s = Solution()
print(s.movingCount(m, n, k))
