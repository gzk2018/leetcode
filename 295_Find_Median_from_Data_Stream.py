class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        stack = self.stack
        l, r = 0, len(stack)
        while l < r:
            m = (l + r) // 2
            if stack[m] >= num:
                r = m
            else:
                l = m + 1
        stack.insert(l, num)

    def findMedian(self):
        """
        :rtype: float
        """
        stack = self.stack
        n = len(stack)
        if n % 2 == 1:
            return stack[n // 2]
        else:
            return (stack[n // 2] + stack[n // 2 - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()