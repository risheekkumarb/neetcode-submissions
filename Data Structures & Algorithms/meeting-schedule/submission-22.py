"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: return True
        intervals.sort(key=lambda x:x.start)
        mins,mine = intervals[0].start, intervals[0].end
        for o in intervals[1:]:
            if mine > o.start: return False
            mine = max(mine,o.end)
        return True