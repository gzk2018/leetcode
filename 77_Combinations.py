class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        nums = [i + 1 for i in range(n)]

        def com(nums, k):
            if k == 1:
                return [[num] for num in nums]
            if len(nums) == k:
                return [nums]
            res = com(nums[:-1], k)
            for before in com(nums[:-1], k - 1):
                res.append(before + [nums[-1]])
            return res

        return com(nums, k)