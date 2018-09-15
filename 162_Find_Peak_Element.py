class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # log(n) 解法
        # 一共分四种情况，nums[m-1], nums[m] 和 nums[m+1]的关系
        def func(start, end):
            if start == end:
                return start
            elif start == end - 1:
                return start if nums[start] > nums[end] else end
            else:
                # 010
                m = (start + end) // 2
                if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                    return m
                # 012
                elif nums[m-1] < nums[m] < nums[m+1]:
                    return func(m+1, end)
                else:
                    return func(start, m-1)
        return func(0, len(nums)-1)