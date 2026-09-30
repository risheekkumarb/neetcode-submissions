import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)

        def timetaken(speed): return sum([math.ceil(float(o)/speed) for o in piles])

        res = r
        while l<r:
            m = (l+r)//2
            ht = timetaken(m)
            if ht <= h:
                res = m
                r = m
            else:
                l = m+1
        return res
