class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        n = len(intervals)
        res = []
        i = 0

        while i < n:
            curr = intervals[i]
            while (
                res 
                and ( curr[0] <= res[-1][0] <= curr[1]
                or curr[0] <= res[-1][1] <= curr[1]
                or res[-1][0] <= curr[0] <= res[-1][1]
                or res[-1][0] <= curr[1] <= res[-1][1])
            ):
                start, end = res.pop()
                start = min(start, curr[0])
                end = max(end, curr[1])
                curr = [start, end]
            res.append(curr)
            i += 1
        
        return res
