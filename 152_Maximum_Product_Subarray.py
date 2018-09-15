class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = maxpro = minpro = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] < 0:
                maxpro, minpro = minpro, maxpro
            maxpro = max(nums[i], maxpro*nums[i])
            minpro = min(nums[i], minpro*nums[i])
            res = max(res, maxpro)
        return res