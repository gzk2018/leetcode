class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0 = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] < 2:
                p0 += 1
                nums[p0], nums[i] = nums[i], nums[p0]
                if nums[p0] == 0:
                    # count记录1的数量，相当于三段切分
                    nums[p0 - count], nums[p0] = nums[p0], nums[p0 - count]
                else:
                    count += 1
