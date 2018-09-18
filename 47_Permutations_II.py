class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def per(nums):
            if len(nums) == 1:
                return [nums]
            res = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                for j in per(nums[:i] + nums[i+1:]):
                    res.append([nums[i]] + j)
            return res
        return per(nums)