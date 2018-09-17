class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #         dp 方法：
        #         n = len(coins)
        #         inf = float('inf')
        #         dp = [[inf for j in range(amount + 1)] for i in range(n)]
        #         for i in range(n):
        #             dp[i][0] = 0
        #         for j in range(1, amount + 1):
        #             if j % coins[0] == 0:
        #                 dp[0][j] = j // coins[0]

        #         for i in range(1, n):
        #             for j in range(1, amount + 1):
        #                 if j < coins[i]:
        #                     dp[i][j] = dp[i-1][j]
        #                 else:
        #                     dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
        #         return dp[-1][-1] if dp[-1][-1] != inf else -1
        coins.sort(reverse=True)
        self.res = 2 ** 31

        def dfs(s, index, count):
            if s == amount:
                self.res = min(self.res, count)
                return
            for i in range(index, len(coins)):
                # 判断条件判断当前是否可能完成，会节省很多时间
                # s + (self.res - count)*coins[i] >= amount
                if s + coins[i] <= amount and s + (self.res - count) * coins[i] >= amount:
                    # if s + coins[i] <= amount and count < self.res:
                    dfs(s + coins[i], i, count + 1)

        dfs(0, 0, 0)
        return self.res if self.res != 2 ** 31 else -1








