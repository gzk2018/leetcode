class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0: return 0

        if k >= len(prices):
            res = 0
            for i in range(len(prices) - 1):
                res += max(0, prices[i + 1] - prices[i])
            return res
        times = k
        n = len(prices)

        dp = [0 for j in range(n)]
        # 这个地方cost要为正，因为后面判断条件为price[i] > cost
        # 如果cost为负的话条件要修改
        cost = prices[0]
        for i in range(1, n):
            if prices[i] > cost:
                dp[i] = max(dp[i - 1], prices[i] - cost)
            else:
                cost = prices[i]
                dp[i] = dp[i - 1]

        for k in range(1, times):
            cost = -prices[0]
            for j in range(1, n):
                up = dp[j]
                dp[j] = max(dp[j - 1], prices[j] + cost)
                cost = max(cost, up - prices[j])
                up = dp[j]
        return dp[-1]
