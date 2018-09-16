from collections import deque
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        flag = False
        stack = deque()
        sums, res = 0, len(nums)
        index = 0
        while index < len(nums):
            stack.append(nums[index])
            sums += nums[index]
            while sums >= s:
                flag = True
                res = min(res, len(stack))
                temp = stack.popleft()
                sums -= temp
            index += 1
        return res if flag else 0