class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for i in range(n)]
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[j] = 1
            else:
                break
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            left = dp[0]
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[j] = dp[j] + left
                else:
                    dp[j] = 0
                left = dp[j]
        return dp[-1]


