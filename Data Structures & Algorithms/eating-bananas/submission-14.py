class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        while l < r:
            m = (l+r) // 2
            if self.calc_h(piles,m) <= h: r=m
            else: l=m+1
        return l
    
    def calc_h(self, piles, k):
        return sum([math.ceil(o/k) for o in piles])
            