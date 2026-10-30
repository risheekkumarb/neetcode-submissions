class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin = float('inf')
        maxp = 0

        for p in prices:
            cmin = min(cmin,p)
            maxp = max(p-cmin,maxp)

        return maxp
    