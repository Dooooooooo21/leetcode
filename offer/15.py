class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        flag = 1

        while flag <= n:
            if n & flag:
                count += 1
            flag = flag << 1
            print(flag)
        print(count)

        return count

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n:
            count += 1
            n = (n - 1) & n

        return count


s = Solution()
s.hammingWeight(0o0000000000000000000000000001011)
