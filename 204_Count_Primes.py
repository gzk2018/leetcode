class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 0

        def isPrime(n):
            if n <= 3: return True
            for i in range(2, n - 1):
                if n % i == 0:
                    return False
            return True

        dp = [1 for i in range(n)]
        dp[0] = dp[1] = 0
        for i in range(2, n):
            # 如果dp[i] = 1，则说明i不存在比他小的因数，所以是质数
            if dp[i] == 1:
                index = 2
                while index * i < n:
                    dp[index * i] = 0
                    index += 1
        return sum(dp)
