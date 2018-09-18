class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i % (n+1)的范围是0-n
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] >= n:
                nums[i] = 0
        # 相当于u是吧0-n范围内的数放置到0-n的位置上
        for i in range(n):
            nums[nums[i]%n] += n
        # 哪个位置为空就说明缺失了哪个数字
        for i in range(n):
            if nums[i] // n == 0:
                return i
        # 都不空的话缺失最后一个数字
        return n