class Solution(object):

    def dfs(self, board, i, j, isvisted, chs, index):
        if index == len(chs):
            return True
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or isvisted[i][j] or board[i][j] != chs[index]:
            return False
        isvisted[i][j] = 1
        res = self.dfs(board, i - 1, j, isvisted, chs, index + 1) \
              or self.dfs(board, i + 1, j, isvisted, chs, index + 1) \
              or self.dfs(board, i, j - 1, isvisted, chs, index + 1) \
              or self.dfs(board, i, j + 1, isvisted, chs, index + 1)
        isvisted[i][j] = 0
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        rows = len(board)
        lines = len(board[0])

        isvisted = [[0] * lines for i in range(rows)]

        for i in range(rows):
            for j in range(lines):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, isvisted, word, 0):
                        return True

        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

s = Solution()
print(s.exist(board, word))
