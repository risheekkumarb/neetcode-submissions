class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n > h: return None
        res = float('inf')
        l,r = 1,max(piles)
        while l <= r:
            m = (l+r) // 2
            if self.calc_h(piles,m) <= h :
                res = m
                r=m-1
            else: l=m+1
        return res
    
    def calc_h(self, piles, k):
        return sum([math.ceil(o/k) for o in piles])
            