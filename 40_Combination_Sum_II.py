class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        def dfs(index, path, s):
            if s == target:
                ret.append(path)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:continue
                if s + candidates[i] <= target:
                    dfs(i + 1, path + [candidates[i]], s + candidates[i])
        dfs(0, [], 0)
        return ret