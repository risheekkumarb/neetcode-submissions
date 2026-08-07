class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # we need a node where everything comes in, nothings goes out.
        t = [0] * (n+1)
        for p,trusts in trust:
            t[trusts] += 1
            t[p] -= 1

        for i,score in enumerate(t):
            if score == n-1: return i
        
        return -1