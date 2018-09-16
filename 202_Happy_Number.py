class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def happy(num):
            res = []
            while num > 0:
                res.append((num % 10) ** 2)
                num //= 10
            return sum(res)

        dic = set()
        while n not in dic:
            dic.add(n)
            nextnum = happy(n)
            if nextnum == 1:
                return True
            n = nextnum
        return False