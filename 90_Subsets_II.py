class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        def per(path, index):
            self.res.append(path)
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:continue
                per(path + [nums[i]], i + 1)
        per([], 0)
        return self.res