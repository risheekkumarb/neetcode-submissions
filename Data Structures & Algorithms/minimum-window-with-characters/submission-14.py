from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        l, have, done = 0,0,len(countT)
        wind = defaultdict(int)
        res = float('inf'), (0,0)

        for r,c in enumerate(s):
            wind[c] += 1
            if c in countT and countT[c] == wind[c]: have += 1
            while have == done:
                if r-l+1 < res[0]: res = r-l+1, (l,r)
                if s[l] in countT and wind[s[l]] == countT[s[l]]: have-=1
                wind[s[l]] -= 1
                l += 1
        
        # return '' if res[0] == float('inf') else s[res[1][1]:res[1][0]+1]
        return '' if res[0] == float('inf') else s[res[1][0]:res[1][1]+1]