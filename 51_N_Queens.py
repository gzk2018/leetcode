class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []

        def isValid(queens, index, pos):
            for i in range(index):
                if pos == queens[i] or index - i == abs(pos - queens[i]):
                    return False
            return True

        def dfs(index, queens, path):
            if index == n:
                res.append(path)
                return

            for i in range(n):
                if isValid(queens, index, i):
                    dfs(index + 1, queens + [i], path + ["." * i + 'Q' + '.' * (n - i - 1)])

        dfs(0, [], [])
        return res