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

        for i in intervals:
            if q and i.start >= q[0]:
                heappop(q)
            heappush(q,i.end)

        return len(q)