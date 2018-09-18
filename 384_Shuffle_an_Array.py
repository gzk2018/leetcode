import copy
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.origin = copy.deepcopy(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = self.nums

        def shu(nums):
            res = []
            while nums:
                index = random.randint(0, len(nums) - 1)
                res.append(nums[index])
                nums[index], nums[-1] = nums[-1], nums[index]
                nums.pop()
            return res

        self.nums = shu(nums)
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()