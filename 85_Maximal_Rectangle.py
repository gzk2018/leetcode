class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:return 0
        def func(nums):
            nums.append(0)
            stack = [-1]
            index, n, res = 0, len(nums), 0
            while index < n:
                while stack and nums[stack[-1]] > nums[index]:
                    temp = stack.pop()
                    res = max(res, (index - stack[-1] - 1) * nums[temp])
                stack.append(index)
                index += 1
            return res
        m, n = len(matrix), len(matrix[0])
        dp = [int(matrix[0][j]) for j in range(n)]
        res = func(dp)
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + 1
            res = max(res, func(dp))
        return res