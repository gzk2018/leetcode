class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #         def helper(n):
        #             res = 0
        #             while n > 0:
        #                 res += n%10
        #                 n //= 10
        #             return res

        #         while num > 9:
        #             num = helper(num)
        #         return num

        return (num - 1) % 9 + 1 if num != 0 else 0