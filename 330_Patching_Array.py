class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        index = count = 0
        # cursum表示目前测试能不能加到的数值
        cursum = 1
        # 经过当前循环后就能达到更新前的cursum
        while cursum <= n:
            if index < len(nums) and nums[index] <= cursum:
                cursum += nums[index]
                # 每个数字只能用一次
                index += 1
            else:
                count += 1
                cursum += cursum
        return count