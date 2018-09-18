class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic and dic[temp] != i:
                return [i, dic[temp]]
            else:
                dic[nums[i]] = i