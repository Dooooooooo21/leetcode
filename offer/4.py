from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        lines = len(matrix[0])

        for i in range(rows):
            for j in reversed(range(lines)):
                if target == matrix[i][j]:
                    return True
                elif target > matrix[i][j]:
                    rows = rows - 1
                else:
                    lines = lines - 1

        return False


input = [[1, 2, 3]]

s = Solution()
print(s.findNumberIn2DArray(input, 1))
