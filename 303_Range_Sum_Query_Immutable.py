class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        dp = [nums[0] for i in range(len(nums))]

        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i]
        self.dp = dp

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = self.dp
        if i == 0:
            return dp[j]
        else:
            return dp[j] - dp[i - 1]

        # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)