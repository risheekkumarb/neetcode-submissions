class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = dict()
        l = 0
        res = 0

        for r,letter in enumerate(s):
            if letter in w:
                l = max(w[letter] + 1, l)
            w[letter] = r
            res = max(res, r-l+1)
        
        return res
