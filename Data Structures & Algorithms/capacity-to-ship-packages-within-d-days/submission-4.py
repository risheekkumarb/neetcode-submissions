class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        while l < r:
            m = (l+r) // 2
            if self.days_req(weights, m) <= days: r=m
            else: l=m+1
        return l

    def days_req(self, weights, capacity):
        days = 0
        load = 0
        for w in weights:
            load += w
            if load > capacity:
                days += 1
                load = w
        return days if load == 0 else days+1