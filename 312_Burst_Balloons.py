class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 相当于矩阵链式乘法
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n)]
        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                for k in range(i+1, j):
                    # dp[i][j]表示从i到j之间最大得分
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
        return dp[0][-1]