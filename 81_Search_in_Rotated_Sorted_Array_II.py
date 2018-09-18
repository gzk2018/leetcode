class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] == nums[left + 1]:left += 1
            while left < right and nums[right] == nums[right - 1]:right -= 1
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        # 这个地方也要往前倒退
        while right > 0 and nums[right] == nums[right-1]:right -= 1
        index = right
        print(index)
        f = lambda x:(x+index)%len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            real_mid = f(mid)
            if nums[real_mid] == target:
                return True
            elif nums[real_mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False