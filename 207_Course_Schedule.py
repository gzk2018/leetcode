class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = {}
        dic = {}
        for x, y in prerequisites:
            if x not in dic:
                dic[x] = []
            dic[x].append(y)

        def dfs(n):
            if n not in dic or visited.get(n, 0) == 1:
                return True
            if visited.get(n, 0) == 2:
                return False

            visited[n] = 2
            for adj in dic[n]:
                if not dfs(adj):
                    return False
            visited[n] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
