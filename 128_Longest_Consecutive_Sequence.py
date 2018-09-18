class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                count = 0
                start = i
                while start in nums:
                    count += 1
                    start += 1
                res = max(res, count)
        return res