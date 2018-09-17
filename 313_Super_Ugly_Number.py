class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        num = len(primes)
        factors = [0 for i in range(num)]
        ugly = [1]
        count = 1
        while count < n:
            candidates = []
            for i in range(num):
                # factors 表示第i个质数乘以第factor[i]个ugly number
                # 这里乘以ugly[factors[i]]
                candidates.append(primes[i]*ugly[factors[i]])
            u = min(candidates)
            for i in range(num):
                if u == candidates[i]:
                    factors[i] += 1
            ugly.append(u)
            count += 1
        return ugly[-1]