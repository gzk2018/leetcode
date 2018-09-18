class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        self.isfind = False

        def dfs(x, y, index):
            if index == len(word) or self.isfind:
                self.isfind = True
                return
            sur = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            temp = board[x][y]
            board[x][y] = '%'
            for posx, posy in sur:
                if 0 <= posx < m and 0 <= posy < n and board[posx][posy] == word[index]:
                    dfs(posx, posy, index + 1)
            board[x][y] = temp

        for i in range(m):
            for j in range(n):
                if not self.isfind and board[i][j] == word[0]:
                    dfs(i, j, 1)
        return self.isfind