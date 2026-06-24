from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''

        tcount = Counter(t)

        w, l = defaultdict(int), 0
        res = (float('inf'), (0,0))
        have, done = len(tcount), 0

        for r, letter in enumerate(s):
            w[letter] += 1
            if letter in tcount and w[letter] == tcount[letter]: done += 1

            while done == have:
                if r-l+1 < res[0]: res = (r-l+1, (l,r))
                leftLetter = s[l]
                if leftLetter in tcount and w[leftLetter] == tcount[leftLetter]: done-=1
                w[leftLetter] -= 1
                l += 1
        
        return s[res[1][0]:res[1][1]+1] if res[0] != float('inf') else ''