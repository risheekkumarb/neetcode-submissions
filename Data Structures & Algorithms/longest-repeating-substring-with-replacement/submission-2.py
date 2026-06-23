from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        w = defaultdict(int)
        l, maxf, res = 0, 0, 0

        for r, letter in enumerate(s):
            w[letter] += 1
            maxf = max(maxf, w[letter])

            while (r-l+1) - maxf > k:
                w[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res
            