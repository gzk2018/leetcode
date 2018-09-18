class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t: return 0
        ns, nt = len(s), len(t)
        # dp[i][j] 表示在s[:j]中有多少种t[:i]
        dp = [[0 for j in range(ns)] for i in range(nt)]
        if s[0] == t[0]: dp[0][0] = 1
        for i in range(1, ns):
            if s[i] == t[0]:
                dp[0][i] = dp[0][i - 1] + 1
            else:
                dp[0][i] = dp[0][i - 1]

        for i in range(1, nt):
            for j in range(1, ns):
                if s[j] == t[i]:
                    # 在s[:j-1]中的t[i] + 在s[:j-1]中的t[:i-1]
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
