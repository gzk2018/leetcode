class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        dp = [0 for i in range(n)]
        for word in wordDict:
            if s[:len(word)] == word:
                dp[len(word) - 1] = 1

        for i in range(1, n):
            if not dp[i - 1]: continue
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    dp[i + len(word) - 1] = 1

        if not dp[-1]: return []
        wordDict = set(wordDict)
        res = []

        def dfs(index, path):
            if index == n:
                res.append(' '.join(path))
                return

            for i in range(index, n):
                if dp[i] == 1 and s[index:i + 1] in wordDict:
                    dfs(i + 1, path + [s[index:i + 1]])

        dfs(0, [])
        return res