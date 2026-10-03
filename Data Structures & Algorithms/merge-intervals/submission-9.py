class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        res = []
        i = 0

        while i < n:
            cur = intervals[i]
            while (
                res and
                (
                    cur[0] <= res[-1][0] <= cur[1]
                    or cur[0] <= res[-1][1] <= cur[1]
                    or res[-1][0] <= cur[0] <= res[-1][1]
                    or res[-1][0] <= cur[1] <= res[-1][1]
                )
            ):
                start,end = res.pop()
                start = min(start, cur[0])
                end   = max(end, cur[1])
                cur = [start, end]
            res.append(cur)
            i+=1

        return res
        