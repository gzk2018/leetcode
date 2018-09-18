class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:return 0
        res = 0
        cost = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > cost:
                res = max(res, prices[i] - cost)
            else:
                cost = prices[i]
        return res