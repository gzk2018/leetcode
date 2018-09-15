class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # res = []
        # while n > 0:
        #     res.append(n % 2)
        #     n = n // 2
        # res += [0] * (32 - len(res))
        # val = 0
        # base = 1
        # for i in range(31,-1,-1):
        #     val += base * res[i]
        #     base *= 2
        # return val
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n = n >> 1
        return ans