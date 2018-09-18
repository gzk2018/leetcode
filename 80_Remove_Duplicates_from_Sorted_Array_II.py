class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index = 0
        res = 0
        while index < n:
            count = 0
            temp = nums[index]
            while index < n and temp == nums[index]:
                if count < 2:
                    nums[index], nums[res] = nums[res], nums[index]
                    res += 1
                count += 1
                index += 1
        return res
