class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited = {}
        dic = {}
        for x, y in prerequisites:
            if x not in dic:
                dic[x] = []
            dic[x].append(y)

        res = []
        self.res = []

        def dfs(n):
            if visited.get(n, 0) == -1:
                return False
            elif visited.get(n, 0) == 1:
                return True
            visited[n] = -1
            for i in dic.get(n, []):
                if not dfs(i):
                    return False
            visited[n] = 1
            # 因为有visited，每门课只会经过一遍，所以可以直接append
            self.res.append(n)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return self.res



