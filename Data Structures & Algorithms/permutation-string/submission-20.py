from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        have, done = 0, len(count1)
        wind = defaultdict(int)
        l = 0

        for r,c in enumerate(s2):
            wind[c] += 1
            if c in count1 and wind[c] == count1[c]: have += 1
            while have == done:
                if r-l+1 == len(s1): return True
                if wind[s2[l]] == count1[s2[l]]: have -= 1
                wind[s2[l]] -= 1
                l += 1
        return False