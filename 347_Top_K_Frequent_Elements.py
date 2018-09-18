from collections import Counter
import random


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = Counter(nums)

        def findk(left, right, nums, k):
            index = random.randint(left, right)
            pivot = nums[index]
            nums[index], nums[right] = nums[right], nums[index]
            j = left - 1
            for i in range(left, right):
                if nums[i] < pivot:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            j += 1
            nums[j], nums[right] = nums[right], nums[j]
            if (j - left) == k:
                return nums[j]
            elif (j - left) > k:
                return findk(left, j - 1, nums, k)
            else:
                return findk(j + 1, right, nums, k - (j - left) - 1)

        v = list(dic.values())
        threshold = findk(0, len(v) - 1, v, len(v) - k)
        res = []
        for key, value in dic.items():
            if value >= threshold:
                res.append(key)
        return res




