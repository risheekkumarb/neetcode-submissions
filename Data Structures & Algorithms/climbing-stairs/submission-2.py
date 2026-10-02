class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}
        def dfs(i):
            if i == n: return 1
            if i > n: return 0
            if i in seen: return seen[i]
            res = dfs(i+1) + dfs(i+2)
            seen[i] = res
            return res
            
        return dfs(0)
        