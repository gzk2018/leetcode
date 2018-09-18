# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        res = self.res
        left, right = 0, len(res)
        while left < right:
            mid = (left + right) // 2
            if res[mid].start >= val:
                right = mid
            else:
                left = mid + 1
        index = right

        # 考虑重复插入的情况
        if (index < len(res) and val == res[index].start) or (index > 0 and val <= res[index - 1].end):
            return
        # 先插入再合并
        res[index:index] = [Interval(val, val)]
        if 0 < index < len(res) - 1 and res[index].start == res[index - 1].end + 1 and res[index].end == res[
            index + 1].start - 1:
            res[index - 1:index + 2] = [Interval(res[index - 1].start, res[index + 1].end)]
        elif index > 0 and res[index].start == res[index - 1].end + 1:
            res[index - 1:index + 1] = [Interval(res[index - 1].start, val)]
        elif index < len(res) - 1 and res[index].end == res[index + 1].start - 1:
            res[index:index + 2] = [Interval(val, res[index + 1].end)]

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()