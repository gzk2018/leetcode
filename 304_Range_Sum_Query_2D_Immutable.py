class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        dp = [[matrix[0][0] for j in range(n)] for i in range(m)]
        for i in range(1, m):
            dp[i][0] = matrix[i][0] + dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = matrix[0][j] + dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]
        self.dp = dp
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        dp = self.dp
        matrix = self.matrix
        if row1 == 0 and col1 == 0:
            return dp[row2][col2]
        elif row1 == 0:
            return dp[row2][col2] - dp[row2][col1 - 1]
        elif col1 == 0:
            return dp[row2][col2] - dp[row1 - 1][col2]
        else:
            return dp[row2][col2] - dp[row1 - 1][col2] - dp[row2][col1 - 1] + dp[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)