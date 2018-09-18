class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = -1
        for j in range(len(nums)):
            if nums[j] != val:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i+1