class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        self.res = 0

        def dfs(x, y):
            if dp[x][y] != 0:
                return dp[x][y]
            sur = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            res = 1
            for i, j in sur:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[x][y]:
                    res = max(res, 1 + dfs(i, j))
            dp[x][y] = res
            return res

        for i in range(m):
            for j in range(n):
                self.res = max(self.res, dfs(i, j))
        return self.res
