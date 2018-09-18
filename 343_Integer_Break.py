class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {2:1,3:2,4:4}
        if n < 5:
            return dp[n]
        if n%3 == 0:
            return 3**(n//3)
        else:
            return max(3**(n//3 - 1) * (n - n//3*3 + 3), 3**(n//3) * (n-n//3*3))