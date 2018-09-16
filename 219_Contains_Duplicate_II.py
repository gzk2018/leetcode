class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = []
            else:
                if i - dic[nums[i]][-1] <= k:
                    return True
            dic[nums[i]].append(i)
        return False
