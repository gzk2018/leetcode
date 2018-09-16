class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def findk(nums, left, right, k):
            pivot = nums[right]
            # 这里时是left-1，如果left，right不是参数的话就是-1
            pointer = left-1
            for i in range(left, right):
                if nums[i] < pivot:
                    pointer += 1
                    nums[pointer], nums[i] = nums[i], nums[pointer]
            pointer += 1
            nums[right], nums[pointer] = nums[pointer], nums[right]
            # 这里是pointer - left，因为left相当于数组的开始，pointer在这个数组中排多少
            if (pointer - left) == k:
                return nums[pointer]
            elif (pointer - left) > k:
                return findk(nums, left, pointer - 1, k)
            else:
                # 最后是k-（pointer-left）-1. 正常情况下是k-pointer-1，但是left才是数组的开始
                return findk(nums, pointer + 1, right, k - (pointer - left) - 1)
        return findk(nums, 0, len(nums)-1, len(nums) - k)