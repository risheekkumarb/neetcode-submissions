class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        for s,e in intervals:
            while res and res[-1][1] >= s:
                ress, rese = res.pop()
                e = max(e, rese)
                s = min(s,ress)
            res.append([s,e])

        return res