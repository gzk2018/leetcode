class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m, n = min(m, n), max(m, n)
        while m < n:
            n = n & (n-1)
        return n