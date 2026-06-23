class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        mL, mR = [[0] * n for _ in range(2)]

        m = 0
        for i,h in enumerate(height):
            m = max(m, h)
            mL[i] = m

        m = 0
        for i,h in enumerate(height[::-1]):
            m = max(m,h)
            mR[n-1-i] = m
        
        res = 0
        for i,h in enumerate(height):
            wh  = min(mL[i], mR[i])
            res += wh - h
        
        return res