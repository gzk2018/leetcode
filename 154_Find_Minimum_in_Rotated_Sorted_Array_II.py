# 和第81题不一样

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            mid = (left + right) // 2
            # 最小值在left到mid之间
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            # 无法判断最小值在哪里，但是right肯定不是最小值
            else:
                right -= 1
        return nums[right]
