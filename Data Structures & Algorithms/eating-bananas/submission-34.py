import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(speed): return sum([math.ceil(o/speed) for o in piles])
        l,r = 1,max(piles)
        res = 0
        while l<=r:
            m = (l+r) // 2
            if get_time(m) <= h:
                res = m
                r = m-1
            else:
                l = m+1
        return res