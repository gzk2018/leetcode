class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        res = []
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and up <= down:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1

            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1

            # 加两个判断条件
            if down >= up:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
