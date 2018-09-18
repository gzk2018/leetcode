class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums.sort()
        target = 0
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            add3 = nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] + add3 == 0:
                    res.append([add3, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + add3 < 0:
                    left += 1
                else:
                    right -= 1
        return res