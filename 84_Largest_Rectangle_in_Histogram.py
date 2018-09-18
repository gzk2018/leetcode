class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        res = 0
        index = 0
        while index < len(heights):
            while stack and heights[index] < heights[stack[-1]]:
                temp = stack.pop()
                res = max(res, (index - stack[-1] - 1) * heights[temp])
            stack.append(index)
            index += 1
        return res