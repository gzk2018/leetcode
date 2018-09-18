class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            x = -x
            flag = -1
        ret = []
        while x > 0:
            ret.append(x % 10)
            x //= 10
        coeff = 1
        num = 0
        for i in range(len(ret) - 1, -1, -1):
            num += ret[i] * coeff
            coeff *= 10
        if num > 2 ** 31: return 0
        return num * flag
