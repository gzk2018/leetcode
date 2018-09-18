# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:return [newInterval]
        if newInterval.end < intervals[0].start:return [newInterval] + intervals
        if newInterval.start > intervals[-1].end:return intervals + [newInterval]
        index, n = 0, len(intervals)
        while index < n:
            if newInterval.start <= intervals[index].end:
                point = index
                start = min(intervals[index].start, newInterval.start)
                end = newInterval.end
                while index < n and newInterval.end >= intervals[index].start:
                    # end 也要随着更新
                    end = max(end, intervals[index].end)
                    index += 1
                intervals[point:index] = [Interval(start, end)]
                break
            index += 1
        return intervals