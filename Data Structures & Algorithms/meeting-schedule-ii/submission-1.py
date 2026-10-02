"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappop,heappush
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        q = [] # end time

        for o in intervals:
            start,end = o.start,o.end
            if q and q[0] <= start:
                heappop(q)
            heappush(q,end)

        return len(q)