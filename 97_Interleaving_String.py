class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if len(s1) + len(s2) != len(s3):return False
        dp = [[0 for j in range(n2 + 1)] for j in range(n1 + 1)]
        dp[0][0] = 1
        for i in range(1, n1+1):
            if s1[i-1] == s3[i-1] and dp[i-1][0]:
                dp[i][0] = 1
        for j in range(1, n2+1):
            if s2[j-1] == s3[j-1] and dp[0][j-1]:
                dp[0][j] = 1
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                # 前提条件dp[i-1][j], s1提供i-1个字符，s2提供j个字符
                if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = 1
                if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = 1
        return dp[-1][-1] == 1