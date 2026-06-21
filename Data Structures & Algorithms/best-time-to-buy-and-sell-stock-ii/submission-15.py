from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, have):
            if i >= len(prices): return 0
            if have == 0:
                return max(dfs(i+1, 1) - prices[i], dfs(i+1, 0))
            else:
                return max(dfs(i+1, 0) + prices[i], dfs(i+1, 1))
        
        return dfs(0, 0)