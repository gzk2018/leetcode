class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(index, path, s):
            if s == n and len(path) == k:
                res.append(path)
                return
            for i in range(index, len(nums)):
                if s + nums[index] <= n and len(path) < k:
                    dfs(i+1, path + [nums[i]], s + nums[i])
        nums = [i+1 for i in range(9)]
        dfs(0, [], 0)
        return res