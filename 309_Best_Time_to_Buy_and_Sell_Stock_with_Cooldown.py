class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:return 0
        n = len(prices)
        # buy[i]表示第i天的成本
        buy = [0 for i in range(n)]
        # sell[i]表示第i天的资本量
        sell = [0 for i in range(n)]
        buy[0], buy[1] = -prices[0], max(-prices[0], -prices[1])
        sell[0], sell[1] = 0, max(0, prices[1] + buy[0])
        for i in range(2, n):
            # 第i天卖出
            sell[i] = max(sell[i-1], prices[i] + buy[i-1])
            # 第i天买入，但是只能从i-2买入
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        return sell[-1]