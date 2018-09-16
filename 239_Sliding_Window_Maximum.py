from collections import deque as dq


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = dq()
        n = len(nums)
        # stack.append(0) 防止只有一个输入且k = 1的情况
        res = []
        for i in range(n):
            # 判断最大的数是否还在k范围内
            if stack and i - stack[0] >= k:
                stack.popleft()
            # 维护一个递减序列
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            # 在当前k范围内最大的数就是stack中最后的下标指向的数
            stack.append(i)
            if i + 1 >= k:
                res.append(nums[stack[0]])
        return res