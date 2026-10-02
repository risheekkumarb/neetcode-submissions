class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        seen = {}
        n = len(cost)
        def dfs(i):
            if i >= n: return 0
            if i in seen: return seen[i]
            seen_cost = cost[i] + min(dfs(i+1),dfs(i+2))
            seen[i] = seen_cost
            return seen_cost
        return min(dfs(0),dfs(1))