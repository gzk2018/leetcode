# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start)
        index = 0
        while index < len(intervals):
            if index < len(intervals)-1 and intervals[index].end >= intervals[index + 1].start:
                intervals[index].end = max(intervals[index].end, intervals[index+1].end)
                intervals[index+1:index+2] = []
            else:
                index += 1
        return intervals