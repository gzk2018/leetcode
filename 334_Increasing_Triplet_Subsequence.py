class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smaller = smallest = 2 ** 31
        for i in range(len(nums)):
            if nums[i] <= smallest:
                smallest = nums[i]
            elif nums[i] <= smaller:
                smaller = nums[i]
            else:
                return True
