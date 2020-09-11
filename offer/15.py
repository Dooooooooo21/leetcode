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

        return count
