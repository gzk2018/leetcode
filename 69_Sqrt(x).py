class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 >= x:
                right = mid
            else:
                left = mid + 1
        return right if right ** 2 == x else right - 1
