class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def threeSum(nums, target):
            ret = []
            n = len(nums)
            for i in range(n - 2):
                if i > 0 and nums[i] == nums[i - 1]: continue
                add1 = nums[i]
                new = nums[i + 1:]
                left, right = 0, len(new) - 1
                while left < right:
                    S = add1 + new[left] + new[right]
                    if S == target:
                        ret.append([add1, new[left], new[right]])
                        while left < right and new[left] == new[left + 1]: left += 1
                        while left < right and new[right] == new[right - 1]: right -= 1
                        left += 1
                        right -= 1
                    elif S > target:
                        right -= 1
                    else:
                        left += 1
            return ret

        nums.sort()
        n = len(nums)
        ret = []
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for r in threeSum(nums[i + 1:], target - nums[i]):
                ret.append([nums[i]] + r)
        return ret

