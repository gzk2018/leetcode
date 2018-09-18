class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 至下而上的dp
        n = len(triangle)
        dp = [triangle[-1][i] for i in range(len(triangle[-1]))]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]