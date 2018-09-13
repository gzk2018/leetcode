class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0 for i in range(n)]
        for word in wordDict:
            if s[:len(word)] == word:
                # dp[0] = 1
                dp[len(word) - 1] = 1

        for i in range(1, n):
            if not dp[i - 1]: continue
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    dp[i + len(word) - 1] = 1
        return dp[-1] == 1
