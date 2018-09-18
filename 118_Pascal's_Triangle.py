from operator import add


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        res = [[1]]
        index = 1
        while index < numRows:
            res.append(list(map(add, [0] + res[-1], res[-1] + [0])))
            index += 1
        return res
