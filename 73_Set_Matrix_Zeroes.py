class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row0 = col0 = 0
        m, n = len(matrix), len(matrix[0])
        # 第一列有没有0
        for i in range(m):
            if matrix[i][0] == 0:
                row0 = 1
                break
        # 第一行有没有0
        for j in range(n):
            if matrix[0][j] == 0:
                col0 = 1
                break
        # 用第一行和第一列来记录这一行或这一列是否应该被置为0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0:
            for i in range(m):
                matrix[i][0] = 0
        if col0:
            for j in range(n):
                matrix[0][j] = 0



