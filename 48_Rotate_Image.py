class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, len(matrix) - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        for j in range(1, len(matrix)):
            for i in range(j):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
