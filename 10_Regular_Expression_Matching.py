class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ns, np = len(s), len(p)
        dp = [[0 for j in range(np + 1)] for i in range(ns + 1)]
        dp[0][0] = 1
        for j in range(2, np + 1):
            if dp[0][j - 2] == 1 and p[j - 1] == '*':
                dp[0][j] = 1

        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] != '.' and p[j - 2] != s[i - 1]:
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1] == 1