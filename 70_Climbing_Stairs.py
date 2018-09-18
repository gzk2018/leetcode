class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return n
        first, second = 1, 2
        res = 0
        for i in range(3, n + 1):
            res = first + second
            first = second
            second = res
        return res