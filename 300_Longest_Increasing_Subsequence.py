class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n^2
        # if not nums:return 0
        # res = 1
        # n = len(nums)
        # dp = [1 for i in range(n)]
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     res = max(res, dp[i])
        # return res

        # nlogn
        if not nums: return 0
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        res = 1
        for i in range(1, n):
            if nums[i] > dp[res - 1]:
                dp[res] = nums[i]
                res += 1
            else:
                left, right = 0, res
                while left < right:
                    mid = (left + right) // 2
                    if dp[mid] >= nums[i]:
                        right = mid
                    else:
                        left = mid + 1
                dp[right] = nums[i]
        return res