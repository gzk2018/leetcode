class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 3: return max(nums)

        def helper(nums):
            dp = [0 for i in range(len(nums))]
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:len(nums) - 1]))