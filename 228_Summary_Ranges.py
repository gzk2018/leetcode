class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        index, n = 0, len(nums)
        while index < n:
            start = end = index
            while index < n-1 and nums[index] + 1 == nums[index+1]:
                end += 1
                index += 1
            if end == start:
                res.append(str(nums[end]))
            else:
                res.append(str(nums[start]) + '->' + str(nums[end]))
            index += 1
        return res