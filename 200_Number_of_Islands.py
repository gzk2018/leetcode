class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0

        def dfs(x, y):
            grid[x][y] = '0'
            surround = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for i, j in surround:
                if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                    dfs(i, j)

        self.res = 0
        m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     if grid[i][0] == '1':
        #         self.res += 1
        #         dfs(i,0)
        #     if grid[i][n-1] == '1':
        #         self.res += 1
        #         dfs(i, n-1)
        # for j in range(1, n):
        #     if grid[0][j] == '1':
        #         self.res += 1
        #         dfs(0,j)
        #     if grid[m-1][j] == '1':
        #         self.res += 1
        #         dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.res += 1
                    dfs(i, j)
        return self.res



