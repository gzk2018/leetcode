class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = index = len(nums) - 1
        for i in range(index, -1, -1):
            if nums[i] + i >= index:
                index = i
        return index == 0
