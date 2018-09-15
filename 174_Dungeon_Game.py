class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])
        for j in range(n - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                up = max(1, dp[i + 1][j] - dungeon[i][j])
                right = max(1, dp[i][j + 1] - dungeon[i][j])
                dp[i][j] = min(up, right)
        return dp[0][0]