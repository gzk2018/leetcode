class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = c = 0
        ugly = [1]
        count = 1
        while count < n:
            # ugly 数字都是由2，3，5乘出来的
            # 后面的ugly number可以由前面的ugly number *（2，3，5）得到
            va, vb, vc = ugly[a]*2, ugly[b]*3, ugly[c]*5
            v = min(va, vb, vc)
            ugly.append(v)
            if v == va:
                a += 1
            if v == vb:
                b += 1
            if v == vc:
                c += 1
            count += 1
        return ugly[-1]