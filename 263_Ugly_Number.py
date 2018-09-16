class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:return False
        # while num%3 == 0 or num%5 ==0 or num%2 ==0:
        #     if num%3==0: num //= 3
        #     if num%5 == 0: num //= 5
        #     if num%2 == 0:num //=2
        # return num <= 5
        for i in [2,3,5]:
            while num%i == 0:num //= i
        return num < 5