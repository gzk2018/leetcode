class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index = 0
        count = 0
        while index < n - 1:
            nextindex = 0
            step = 0
            for i in range(1, nums[index] + 1):
                if i + index >= n - 1:return count + 1
                if i + index + nums[i + index] >= nextindex:
                    nextindex = index + i + nums[i + index] # 数组的下标是i+index，不是i
                    step = i
            index += step
            count += 1
        return count