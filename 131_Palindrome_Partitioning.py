class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
        res = []

        def dfs(x, path):
            if x == n:
                res.append(path)
                return

            for i in range(x, n):
                if dp[x][i] == 1:
                    dfs(i + 1, path + [s[x:i + 1]])

        dfs(0, [])
        return res