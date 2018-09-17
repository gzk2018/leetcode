class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, n = -1, len(nums)
        for j in range(n):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
