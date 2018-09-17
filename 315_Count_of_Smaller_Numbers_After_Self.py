class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newArray = []
        res = []
        for i in range(len(nums) -1, -1, -1):
            target = nums[i]
            left, right = 0, len(newArray)
            while left < right:
                mid = (left + right) // 2
                if newArray[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            res.append(right)
            newArray.insert(right, target)
        return res[::-1]