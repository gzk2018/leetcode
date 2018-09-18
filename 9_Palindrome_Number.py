class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        if x < 0:
            return False
        res = []
        while x > 0:
            res.append(x%10)
            x //= 10
        base = 1
        for i in range(len(res)-1, -1,-1):
            num -= res[i]*base
            base *= 10
        return num == 0