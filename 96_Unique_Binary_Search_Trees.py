class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:return 1
        elif n < 3:return n
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[-1]