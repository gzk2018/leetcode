class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        # Any live cell with two or three live neighbors lives on to the next generation.
        # Any live cell with more than three live neighbors dies, as if by over-population..
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        m, n = len(board), len(board[0])

        def count(x, y):
            sur = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i, j) != (0, 0):
                        sur.append((x + i, y + j))
            c = 0
            for i, j in sur:
                if 0 <= i < m and 0 <= j < n:
                    if board[i][j] in {1, 2}:
                        c += 1
            return c

        for i in range(m):
            for j in range(n):
                c = count(i, j)
                # live -> die
                if board[i][j] == 1 and c < 2:
                    board[i][j] = 2
                # live -> live
                elif board[i][j] == 1 and (c == 2 or c == 3):
                    board[i][j] = 1
                # live -> die
                elif board[i][j] == 1 and (c > 3):
                    board[i][j] = 2
                # die -> live
                elif board[i][j] == 0 and c == 3:
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] in {1, 3}:
                    board[i][j] = 1
                elif board[i][j] in {0, 2}:
                    board[i][j] = 0