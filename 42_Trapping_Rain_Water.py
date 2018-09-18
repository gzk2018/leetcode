class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:return 0
        left, right = 0, len(height) - 1
        leftmax, rightmax = height[left], height[right]
        amount = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    amount += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    amount += rightmax - height[right]
                right -= 1
        return amount