class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # -7,1          or 0,0
        # -7,1 or -6,0 | 0,0 or -1,1
        # make profit everyday
        # dont buy if you cant make profit

        profit = 0

        for prev, new in zip(prices[:-1], prices[1:]):
            if new > prev: profit += new - prev

        return profit