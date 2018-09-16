class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or t < 0:return False
        stack = {}
        for i in range(len(nums)):
            # 用bucket来代表一个桶内所有的值
            # 落在一个桶里的值相差小于t，不会出现后面的值覆盖前面的值
            # 整除（t+1）后得到相同的值，相差一定小于t

            newnum = nums[i] // (t+1)
            if newnum in stack:
                return True
            if newnum + 1 in stack and abs(stack[newnum + 1] - nums[i]) <= t:
                return True
            if newnum - 1 in stack and abs(stack[newnum - 1] - nums[i]) <= t:
                return True
            stack[newnum] = nums[i]
            if len(stack) > k:
                del stack[nums[i - k] // (t+1)]
        return False
