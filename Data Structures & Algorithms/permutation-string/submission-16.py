from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1: return False

        w = defaultdict(int)
        count1 = Counter(s1)
        have, done = len(count1), 0
        l = 0

        for r, letter in enumerate(s2):
            w[letter] += 1
            if letter in count1 and count1[letter] == w[letter]: done += 1
            while done == have:
                if len(s1) == r-l+1: return True
                leftLetter = s2[l]
                if leftLetter in count1 and count1[leftLetter] == w[leftLetter]: done -= 1
                l += 1
                w[leftLetter] -= 1
            
        return False