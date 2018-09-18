class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def per(nums):
            if len(nums) == 1:
                return [nums]
            res = []
            for i in range(len(nums)):
                for j in per(nums[:i] + nums[i + 1:]):
                    res.append([nums[i]] + j)
            return res

        return per(nums)
