class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            ans += (n & 1)
            n = n >> 1
        return ans
