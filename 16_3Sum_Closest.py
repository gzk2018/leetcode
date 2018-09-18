class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ret = float('inf')
        for i in range(n):
            add1 = nums[i]
            remain = nums[:i] + nums[i+1:]
            left = 0
            right = len(remain) - 1
            while left < right:
                S = add1 + remain[left] + remain[right]
                if S == target:
                    return target
                elif S > target:
                    right -= 1
                    if abs(S-target) < abs(ret - target):
                        ret = S
                else:
                    left += 1
                    if abs(S - target) < abs(ret - target):
                        ret = S
        return ret