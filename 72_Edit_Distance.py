class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # if not word1:return len(word2)
        n1, n2 = len(word1), len(word2)
        dp = [i for i in range(n2 + 1)]
        for i in range(1, n1 + 1):
            left, leftup = i, i - 1
            dp[0] = left
            for j in range(1, n2 + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = leftup
                else:
                    dp[j] = min(left, leftup, dp[j]) + 1
                left = dp[j]
                leftup = temp
        return dp[-1]