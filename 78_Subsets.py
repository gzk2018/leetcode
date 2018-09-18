class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def dfs(path, index):
            res.append(path)
            if index == n:
                return

            for i in range(index, n):
                dfs(path + [nums[i]], i + 1)

        dfs([], 0)
        return res