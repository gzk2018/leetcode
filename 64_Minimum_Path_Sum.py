class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [0 for j in range(n)]
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]
            left = dp[0]
            for j in range(1, n):
                dp[j] = min(left, dp[j]) + grid[i][j]
                left = dp[j]
        return dp[-1]