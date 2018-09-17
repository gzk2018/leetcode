class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp
        square = set()
        index = 1
        s = index ** 2
        while s <= n:
            square.add(s)
            index += 1
            s = index ** 2
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            if i in square:
                dp[i] = 1
            else:
                for j in square:
                    if j < i:
                        dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1]

        # dfs
#         square = []
#         index = 1
#         s = index ** 2
#         while s <= n:
#             square.append(s)
#             index += 1
#             s = index **2

#         self.res = n
#         square = square[::-1]
#         def dfs(s, count, index):
#             if s == n or count > self.res:
#                 self.res = min(self.res, count)
#                 return

#             for i in range(index, len(square)):
#                 if s + square[i] <= n:
#                     dfs(s + square[i], count+1, index)
#         dfs(0, 0, 0)
#         return self.res

