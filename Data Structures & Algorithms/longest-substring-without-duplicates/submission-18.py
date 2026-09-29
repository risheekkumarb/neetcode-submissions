
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wind = {}
        res,l  = 0,0

        for r,c in enumerate(s):
            if c in wind:
                l = max(wind[c]+1,l)
            wind[c] = r
            res = max(res, r-l+1)

        return res
