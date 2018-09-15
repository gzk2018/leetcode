class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        base = 5
        while n//base > 0:
            res += n // base
            base *=5
        return res
