class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        index = right
        if right >= len(nums) or nums[right] != target:
            return [-1, -1]

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= (target + 1):
                right = mid
            else:
                left = mid + 1
        return [index, right - 1]

