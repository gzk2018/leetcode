class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (j - i == 1 or dp[i+1][j-1]):
                    dp[i][j] = 1
        cut = [n for i in range(n)]
        cut[0] = 0
        for j in range(1, n):
            for i in range(j+1):
                if dp[0][j] == 1:
                    cut[j] = 0
                    break
                elif i != 0 and dp[i][j] == 1:
                    cut[j] = min(cut[j], cut[i-1] + 1)
        return cut[-1]