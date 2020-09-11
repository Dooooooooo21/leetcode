class Solution:
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        for c in s:
            if c == ' ':
                result.append('%20')
            else:
                result.append(c)

        return ''.join(result)


input = [[1, 2, 3]]
s = "We are happy."

solution = Solution()
print(solution.replaceSpace(s))
