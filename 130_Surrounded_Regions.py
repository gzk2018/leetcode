class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:return
        m, n = len(board), len(board[0])
        def dfs(x, y):
            board[x][y] = 'o'
            surround = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for i, j in surround:
                if 0 <= i < m and 0 <= j < n:
                    if board[i][j] == 'O':
                        # board[i][j] = 'o'
                        dfs(i,j)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)
        for j in range(1, n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'o':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'