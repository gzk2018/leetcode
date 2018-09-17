import random


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def findk(nums, left, right, k):
            index = random.randint(left, right)
            # random 以后要换位置
            nums[right], nums[index] = nums[index], nums[right]
            pivot = nums[right]
            j = left - 1
            for i in range(left, right):
                if nums[i] < pivot:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            j += 1
            nums[j], nums[right] = nums[right], nums[j]
            if j - left == k:
                return nums[j]
            elif j - left > k:
                return findk(nums, left, j - 1, k)
            else:
                return findk(nums, j + 1, right, k - (j - left) - 1)

        n = len(nums)
        new = [None for i in range(n)]
        mid = findk(nums, 0, n - 1, n // 2)
        print(mid)
        if n % 2 == 1:
            even = n - 1
        else:
            even = n - 2
        odd = 1
        for i in range(n):
            if nums[i] > mid:
                new[odd] = nums[i]
                odd += 2
            elif nums[i] < mid:
                new[even] = nums[i]
                even -= 2
        for i in range(n):
            if new[i] == None:
                new[i] = mid
        nums[::] = new
