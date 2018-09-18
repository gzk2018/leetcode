class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxlen = 1
        start = end = 0
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n): dp[i][i] = 1
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i < 2):
                    dp[i][j] = 1
                    length = j - i + 1
                    if length > maxlen:
                        maxlen, start, end = length, i, j

        return s[start:end + 1]
