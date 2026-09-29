class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wind = defaultdict(int)
        res,l = 0,0
        maxf = 0

        for r,c in enumerate(s):
            wind[c] += 1
            maxf = max(maxf, wind[c])
            while (r-l+1)-maxf-k > 0:
                wind[s[l]] -= 1
                l+= 1
            res = max(res,r-l+1)

        return res