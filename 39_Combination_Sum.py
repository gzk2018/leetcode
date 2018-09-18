class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret = []

        def dfs(index, path, s):
            if s == target:
                ret.append(path)
                return

            for i in range(index, len(candidates)):
                if s + candidates[i] <= target:
                    dfs(i, path + [candidates[i]], s + candidates[i])

        dfs(0, [], 0)
        return ret