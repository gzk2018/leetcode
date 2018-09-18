class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp
